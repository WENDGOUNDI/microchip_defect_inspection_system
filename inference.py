from ultralytics import YOLO

image = "your microchip image"
prediction_model = YOLO("./app_files/weights/best.pt")

def microchip_status_prediction(predict_img, model):
    model.predict(source=predict_img,conf=0.5, save=True, project='./app_files/', name='predicted_images/', exist_ok=True, verbose=False)
    names = model.names
    predicted_label = " "
    for r in results:
        for c in r.boxes.cls:
            predicted_label = names[int(c)]

    return predicted_label

if __name__ == "__main__":
        print(f"Predicted Label: {microchip_status_prediction(image, prediction_model)}")