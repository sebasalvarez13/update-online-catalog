#!/usr/bin/env python3

import os
import re
from PIL import Image

src_folder = "/home/student-03-48a06b3cf91e/supplier-data/images"
dest_folder = "/home/student-03-48a06b3cf91e/supplier-data/images/"
files = os.listdir(src_folder)
for file in files:
    #use re.search to capture the name of the file without format extension
    result = re.search(r"(\w*)\.", file)
    if result:
        old_name = result[1]
        #define a new name with the original name of file plus the correct format extension
        new_name = old_name + ".jpeg"
        #open image file using its source path
        im = Image.open(os.path.join(src_folder, file))
        # Provide the target width and height of the new image using the rotated image
        (width, height) = (600, 400)
        im_resized = im.resize((width, height))
        #JPG does not support transparency - RGBA means Red, Green, Blue, Alpha - Alpha is transparency.
        #we need to discard the Alpha Channel or save as something that supports transparency - like PNG.
        #The Image class has a method convert which can be used to convert RGBA to RGB -
        #after that you will be able to save as JPG.
        im_formated = im_resized.convert("RGB")
        im_formated.save(dest_folder + new_name, format = "JPEG")
