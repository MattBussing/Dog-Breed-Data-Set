from PIL import Image
import os
import tkinter
from tkinter import Tk, Canvas, PhotoImage
import shutil
import matplotlib.pyplot as plt
import cv2


files = []
count = 0

ORIGINAL = "Images"
OLD = 'OldImages'
execution_path = os.getcwd()

start_working = False
last_location = ''
if last_location == '':
    start_working = True

# copy directory tree
# check if it exists
if OLD not in os.listdir(execution_path):
    print('creating file tree')
    shutil.copytree(src=ORIGINAL, dst=OLD,
                    ignore=shutil.ignore_patterns('*.jpg'))
else:
    print('file tree already created')


# iterate through files and display them
# iterate through each breed
location = execution_path + '/' + ORIGINAL
for current_breed in os.listdir(location):

    # iterate over dog photos in breed
    print('looking at: ' + current_breed)
    image_base_location = location + '/' + current_breed
    for filename in os.listdir(image_base_location):

        pair = current_breed + '/' + filename
        print(current_breed + '/' + filename)
        if pair == last_location:
            print('at location beggining')
            start_working = True
        
        # image?
        if filename.endswith(".jpg") and start_working:
            # file to work with
            image = image_base_location + '/' + filename
            # show image
            # Image.open(image).show()
            # img = cv2.imread(image, cv2.IMREAD_COLOR)
            # cv2.imshow('image2', img)
            tk = Tk()
            canvas = Canvas(tk)
            canvas.pack()
            img = PhotoImage(Image.open(image))
            canvas.create_image((0, 0), img)

            # potentially move
            while True:
                change = input('move (y/n):')
                if change == 'y':
                    backup_loc = image_base_location.replace(
                        ORIGINAL, OLD) + '/' + filename
                    shutil.move(image, backup_loc)
                    print('moved')
                    break
                elif change == 'n':
                    print('not moving')
                    break
                elif change == 'exit':
                    print(pair)
                    exit(1)
                else:
                    print('error y or n')
