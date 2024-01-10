

#! /usr/bin/env python3
import PIL
from PIL import Image
import os

"""
1.write script changeImage.py for images in path ~/supplier-data/images
Size: Change image resolution from 3000x2000 to 600x400 pixel
"""
 
path = './supplier-data/images/' 

for f in os.listdir(path):
    #add condition if images have special name
    if f.endswith('.tiff'): 
        img = Image.open(path + f)
        new_img = img.convert('RGB').resize((600,400))
        filename = f.split('.')[0] #take the name 
        new_img.save('./supplier-data/images/{}.jpeg'.format(filename))
