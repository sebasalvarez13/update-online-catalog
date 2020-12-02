#!/usr/bin/env python3

import os
import requests
import re

src_folder = "/home/student-03-48a06b3cf91e/supplier-data/descriptions/"
description_files = os.listdir(src_folder)
url = "http://34.70.250.179/fruits/"
image_folder = "/home/student-03-48a06b3cf91e/supplier-data/images/"

for file in description_files:
    with open(src_folder + file, "r") as open_description:
        reader = open_description.read().split("\n")
        description_dict = {"name": reader[0], "weight": reader[1], "description": reader[2]}
        #process weight value to obtain an integer instead of a string
        weight_split = description_dict["weight"].split()
        weight_int =int(weight_split[0])
        #assign integer value to dictionary key
        description_dict["weight"] = weight_int
        #add image entry to dictionary. image files have the same name as text files but extension .jpeg instead
        result = re.search(r"(\w*)\.", file)
        description_dict["image_name"] = result[1] + ".jpeg"
        response = requests.post(url, data = description_dict)
        print(response.raise_for_status())
