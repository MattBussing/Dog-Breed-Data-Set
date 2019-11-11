from PIL import Image
import os
import shutil
import matplotlib.pyplot as plt

files = []
count = 0

ORIGINAL = "Images"
OLD = 'OldImages'
execution_path = os.getcwd()


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
        # image?
        if filename.endswith(".jpg"):
            image = image_base_location + '/' + filename
            # show image
            Image.open(image).show()

            print(image_base_location)
            print()
            # potentially move
            while True:
                change = input('move (y/n):')
                if change == 'y':
                    backup_loc = image_base_location.replace(
                        ORIGINAL, OLD) + '/' + filename
                    shutil.move(image, backup_loc)
                elif change == 'n':
                    print('not moving')
                else:
                    print('error y or n')
