#! usr/bin/env python3

import requests
import os

path = './supplier-data/images/' # same location as .tiff images from previous step
url = 'http://localhost/upload' #

for f in os.listdir(path):
    if f.endswith('.jpeg'):
        with open(path+f, 'rb') as img:
            r=requests.post(url, files={'file': img})
