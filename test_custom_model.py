# Import libraries
from super_gradients.training import models

# Initialize the model
best_model = models.get('yolo_nas_l',
                        num_classes=1,
                        checkpoint_path="checkpoints/Train_1/ckpt_best.pth",
                        )
##### INFERENCE ON SINGLE IMAGE
# Test image path
test_image = '/home/abdoul/projects/Kunsan_Soldering_Defect_Inspection/split_dataset/test/images/Image__2023-09-04__14-34-10.png'
#test_image = 'NG_printing/Image__2023-08-21__11-16-46.png'

# uncomment below line to save the predicted image
#best_model.predict(test_image, conf=0.5,).save("output_folder")

# uncomment below line to visualize the predicted image
best_model.predict(test_image, conf=0.6).show()   #save("./inference_output")

###### BELOW CODE EXTRACT THE LABELS AND THE BOUNDING BOX
predictions = best_model.predict(test_image, conf=0.6)
prediction_objects = list(predictions._images_prediction_lst)[0]
bboxes = prediction_objects.prediction.bboxes_xyxy

int_labels = prediction_objects.prediction.labels.astype(int)
class_names = prediction_objects.class_names
pred_classes = [class_names[i] for i in int_labels]
print(pred_classes)
print(bboxes)



