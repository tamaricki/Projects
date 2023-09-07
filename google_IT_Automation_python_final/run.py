
#! usr/bin/env python3

import requests
import os 


#script 
# which will POST fruit images and their respective descriptions in JSON format (run.py)
#The script should turn the data into a JSON dictionary by adding all the required fields, 
# including the image associated with the fruit (image_name, example "image_name": "010.jpeg)
# and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library

fruit_dict = {'name':'', 'weight':'', 'description':'', 'image_name':''}

img_path = './supplier-data/images'
text_path = '/supplier-data/descriptions'
img_sorted = sorted([img for img in os.listdir(img_path) if '.jpeg' in img])
text_sorted = sorted([t for t in os.listdir(text_path)])


for f in range(len(text_sorted)):
    with open(text_path+text_sorted[f], 'r') as text:
        lines = [t.strip() for t in text.readlines()]    
        fruit_dict['name'] = lines[0]
        fruit_dict['weight'] = int(lines[1].split(' ')[0])
        fruit_dict['description'] = ' '.join(lines[2:])
        fruit_dict['image_name'] = img_sorted[f]
    request = requests.post('http://[linux-instance-external-IP]/fruits/', json = fruit_dict)
    if not request.ok:
        raise Exception(request.status_code, f)
