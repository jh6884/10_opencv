import easyocr
import cv2
import matplotlib.pyplot as plt

img_path = '../img/chinese_tra.jpg'
reader = easyocr.Reader(['ch_tra', 'en'], gpu=False)

result = reader.readtext(img_path)

img = cv2.imread(img_path)

plt.figure(figsize = (8,8))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()