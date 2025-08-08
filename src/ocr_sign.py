import numpy as np
import cv2, os, easyocr
import matplotlib.pyplot as plt

path = '../img/'
name = 'signs.jpg'

img = cv2.imread(os.path.join(path+name))

reader = easyocr.Reader(['ko'], gpu=False)
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
    # print(x,y,w,h)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    if type(text) is int:
        cv2.putText(img, f'제한속도: {text}', (x, y-30), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
    else: print(f'전방 {text}입니다.')

plt.figure(figsize=(8,8))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()