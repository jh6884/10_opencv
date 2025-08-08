import numpy as np
import cv2
import easyocr
import os

path = '../img/'
name = 'signs.jpg'

img = cv2.imread(os.path.join(path+name))

reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext(os.path.join(path+name))

for bbox, text, conf in result:
    xs = []
    ys = []
    for i in bbox:
        xs.append(i[0])
        ys.append(i[1])
    x = min(xs)
    y = min(ys)
    w = abs(max(xs)-min(xs))
    h = abs(max(ys)-min(ys))
    print(x,y,w,h)