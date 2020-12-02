#!/usr/bin/env python3

import requests
import os
import re

url = "http://34.70.250.179/upload/"
src_folder = "/home/student-03-48a06b3cf91e/supplier-data/images/"

upload_files_list = os.listdir(src_folder)
for file in upload_files_list:
    result = re.search(r"(\w*.jpeg)", file)
    if result:
        with open(src_folder + result[1], "rb") as open_image:
            response = requests.post(url, files =  {"file": open_image})
