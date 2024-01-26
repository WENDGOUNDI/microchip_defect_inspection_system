# Microchip Defect Inspection System
The aim of this project is to create a python desktop application for microchip defect inspection. The model has been trained via Yolov8n. 
The app interface will be implemented with pysimplegui, a python framework used for building desktop applications.

# Dependency
 - Ulatrlytics
 - OpenCV
 - PySimpleGui
 - PIL

# Datasets
The dataset used here is large of 299 images, downloaded from roboflow. It contents 3 different classes: bent, broken and intact. The data ratio is 208 images, 58 images and 33 images respectively for training data, validation data and testing data.

# How To Run
In order to sucessfully run this project, adjust the paths according to your directory in the .py files.
 - create a python environment and install the depencies
 - run **microship_train_yolov8.py** file for training a new model. You can adjust the paths and select the desired model. Here, Yolov8n is the base model. You can find the trained weight in the **app_files** folder.
 - run **inference.py** for testing the trained model.
 - run **app_gui.py** to launch the desktop app.

# System Overview
## Training System Overview
![training_system_overview](https://github.com/WENDGOUNDI/microchip_defect_inspection_system/assets/48753146/44838330-eab4-4b92-a1e3-e2c312a36472)

## Inference (desktop App) Overview
![inference_system_overview](https://github.com/WENDGOUNDI/microchip_defect_inspection_system/assets/48753146/bea7e4f2-7429-41b6-a3ea-63aa2abd360c)


# Training Performance
### Plotting Metrics
![plot_metrics](https://github.com/WENDGOUNDI/microchip_defect_inspection_system/assets/48753146/9836ba86-ff65-4fa8-8d40-e9c9cd37470b)

### Plotting Training and Validation Loss
![plot_train_val_loss](https://github.com/WENDGOUNDI/microchip_defect_inspection_system/assets/48753146/ad17a4b3-7c47-4d13-b7cc-ab79c4620d49)

### Visualizing Training Labels Classification
![training_classification](https://github.com/WENDGOUNDI/microchip_defect_inspection_system/assets/48753146/6c84002d-2c8b-4ac5-87fe-277aec10bc0a)

# Inference
![inference_1](https://github.com/WENDGOUNDI/microchip_defect_inspection_system/assets/48753146/0efc273c-e67c-4ad8-90d9-42dc91725fda)
![inference_2](https://github.com/WENDGOUNDI/microchip_defect_inspection_system/assets/48753146/3d72e523-29aa-4268-88ae-27f2dc6652e7)
![inference_3](https://github.com/WENDGOUNDI/microchip_defect_inspection_system/assets/48753146/9cbc8cc5-f266-4fb3-a1cb-b8f0b4a0d507)

# Reference
 - dataset link: https://universe.roboflow.com/mvi-assignment/mvi-xg3zr
