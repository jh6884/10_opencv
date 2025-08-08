import numpy as np
import cv2
import easyocr

path = '../img/'
name = 'signs.jpg'

img = cv2.imread(path+name)

reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext(img)

for bbox, text, conf in result:
    print(bbox)

print(result)