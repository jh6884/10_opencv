import numpy as np
import cv2, os, easyocr
import matplotlib.pyplot as plt
from difflib import SequenceMatcher

# 초기 변수 설정
path = '../img/'
name = 'signs.jpg'

# 이미지 읽기
img = cv2.imread(os.path.join(path+name))

# ocr 정의
reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext(os.path.join(path+name))

# 텍스트 대치를 위한 리스트
examples = ['정지', '횡단보도', '자전거횡단', '어린이보호']

# 동작 코드
for bbox, text, conf in result:
    xs = []
    ys = []
    # 좌표 받아오기
    for i in bbox:
        xs.append(i[0])
        ys.append(i[1])
    x = min(xs)
    y = min(ys)
    w = abs(max(xs)-min(xs))
    h = abs(max(ys)-min(ys))
    # print(x,y,w,h)
    # 문자 주변으로 바운딩박스 그리기
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    # 받아온 문자가 숫자인 경우 제한속도를 출력,
    # 글자인 경우 전방에 표지판이 있음을 알림
    try:
        int(text)
        prt_text = f'speed limit: {text} km/h'
        cv2.putText(img, prt_text, (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
        print(f'제한속도 {text} km/h')
    except: 
        # print(text, 'checked')
        for t in examples:
            if SequenceMatcher(None, text, t).ratio() >= 0.5:
                text = t
                break
        # print(text)
        print(f'전방 {text} 입니다.')
            
# 이미지 표시
plt.figure(figsize=(8,8))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()