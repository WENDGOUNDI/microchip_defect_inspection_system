from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')

model.train(
   data='data.yaml',
   imgsz=640,
   batch=4,
   epochs=500)
