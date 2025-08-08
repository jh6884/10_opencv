import pytesseract
import cv2
import matplotlib.pyplot as plt

img_path = '../img/chinese_tra.jpg'
# img_path = '../img/'

img = cv2.imread(img_path)

# 이미지 불러오기
# plt.figure(figsize = (8,8))
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

# 이미지 텍스트 인식
data = pytesseract.image_to_data(img_path, lang='chi_tra+eng', output_type=pytesseract.Output.DICT)
print(data)

# 인식된 텍스트 확인해보기
THRESHOLD = 0.5

