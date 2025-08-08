import pytesseract
import cv2
import matplotlib.pyplot as plt

tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_path = '../img/chinese_tra.jpg'
# img_path = '../img/'

img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 이미지 불러오기

# 이미지 텍스트 인식
string = pytesseract.image_to_string(img_rgb)
print(string)

# 인식된 텍스트 확인해보기
THRESHOLD = 0.5

