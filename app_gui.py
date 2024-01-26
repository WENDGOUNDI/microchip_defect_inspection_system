import io
import os
import PySimpleGUI as sg
from PIL import Image
import cv2
from ultralytics import YOLO

prediction_model = YOLO("./app_files/weights/best.pt")

image = Image.open("./A_black_image.jpg")
image.thumbnail((400, 400))
bio = io.BytesIO()
image.save(bio, format="PNG")

image2 = Image.open("./Color-blue.jpeg")
image2.thumbnail((400, 400))
bio2 = io.BytesIO()
image2.save(bio2, format="PNG")

def microchip_status_prediction(predict_img, model):
    results = model.predict(source=predict_img,conf=0.5, save=True, project='./app_files/', name='predicted_images/', exist_ok=True, verbose=False)
    names = model.names
    predicted_label = " "
    for r in results:
        for c in r.boxes.cls:
            predicted_label = names[int(c)]

    return predicted_label


layout = [[sg.Text("MICROCHIP DEFECT CLASSIFICATION SYSTEM", font=' bold 24',justification='center',size=(50,1))],
          [sg.Image(data=bio.getvalue(), key="-IMAGE INP-", expand_x=False, expand_y=False),
           sg.Image(data=bio2.getvalue(), key="-IMAGE OUT-")],
          [sg.FileBrowse('Get Image', key="-FILE-",target="-FILE-", enable_events=True, font=' bold 15'), 
           sg.Button('Inspect', key='-Inspect-', font=' bold 15')],
         [sg.Multiline(key='-RESULT WIN-',justification='center', size=(100,5))]]
          

window = sg.Window("MICROCHIP DEFECT CLASSIFICATION SYSTEM", layout, resizable=False)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
        
    if event == "-FILE-":
        print(values["-FILE-"])
        inp_image = cv2.imread(values["-FILE-"])
        print(inp_image.shape)
        inp_image = cv2.resize(inp_image, (400, 400))
        print(inp_image.shape)
        imgbytes_in = cv2.imencode(".png", inp_image)[1].tobytes()
        window["-IMAGE INP-"].update(data=imgbytes_in)
        
    if event == "-Inspect-":
        if not values["-FILE-"]:
            pass
        else:
            label_result = microchip_status_prediction(values["-FILE-"], prediction_model)
            predicted_image_path = "./app_files/predicted_images/"+values["-FILE-"].split("/")[-1]
            out_image = cv2.resize(cv2.imread(predicted_image_path), (400, 400))
            imgbytes_out = cv2.imencode(".png", out_image)[1].tobytes()
            window["-IMAGE OUT-"].update(data=imgbytes_out)
            if label_result in ['bent', 'broken']:
                display_message = f"Your microchip is {label_result}. It needs to be fixed."
                window['-RESULT WIN-'].update(display_message, background_color="red")
            else:
                display_message = f"Your microchip is {label_result}. Good to go."
                window['-RESULT WIN-'].update(display_message, background_color="green")
        
window.close()