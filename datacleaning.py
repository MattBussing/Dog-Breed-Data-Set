from imageai.Detection import ObjectDetection
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path,"yolo.h5"))
detector.loadModel()
custom = detector.CustomObjects(dog=True)
files = []
count =0
dirs = os.listdir(os.path.join(execution_path, "images/Images/"))

for onedir in dirs:
    dirsplit = onedir.split('/')
    os.makedirs(os.path.join(execution_path,"NewImages",dirsplit[-1]), exist_ok=True)
    templist = os.listdir(os.path.join(execution_path, "images/Images/",onedir))
    mystring = ((os.path.join(execution_path, "images/Images/",onedir)))
    files.append([mystring + "/" +s for s in templist])
    

flattened = [val for sublist in files for val in sublist]
print(flattened[:10])
for filename in flattened:
    if filename.endswith(".jpg"):
        filenamesplit = filename.split('/')
        detections, objects_path = detector.detectCustomObjectsFromImage(custom_objects=custom,input_image=filename,extract_detected_objects=True,output_image_path=os.path.join(execution_path,"test.jpg"), minimum_percentage_probability=30)
    for eachObjectPath in objects_path:
        os.rename(os.path.join(execution_path,"test.jpg-objects", eachObjectPath), os.path.join(execution_path,"NewImages",filenamesplit[-2],(str(count) + "dog.jpg")))
    count+=1
    for eachObject, eachObjectPath in zip(detections, objects_path):
        print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
        print("Object's image saved in " + eachObjectPath)
        print("-----------------------")
