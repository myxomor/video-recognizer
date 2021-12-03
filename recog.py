import time
import cv2
import numpy as np
import pyautogui as pyautogui
import pytesseract as pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

gray = cv2.imread('text_1.png', cv2.IMREAD_GRAYSCALE)
gray2 = cv2.addWeighted( gray, 1.5, gray, 0, 0.5)
img = gray2
# blur = cv2.GaussianBlur(img,(3,3),1)

# cv2.imshow('blur',blur)
#imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ret = cv2.Canny(imgray,200,255, L2gradient=True)
#
# cv2.imshow('Canny',ret)

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# hsv_min = np.array((17,50,110), np.uint8)
# hsv_max = np.array((101,140,180), np.uint8)
# thresh = cv2.inRange(hsv, hsv_min, hsv_max )
# img_binary = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow('Canny',img_binary)
#
# contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# imgcontr = cv2.drawContours(img_binary, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 0)
# cv2.imshow('contours', imgcontr)
# cv2.drawContours(img_binary, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 2)


print(pytesseract.image_to_string(img,  lang='rus'))

# data = pytesseract.image_to_data(img,  lang='rus')

# for i, el in enumerate(data.splitlines()):
#     if i ==0:
#         continue
#     el = el.split()
#     try:
#         x,y,w,h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
#         cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 1)
#         cv2.putText(img, el[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)
#     except IndexError:
#         print("No")

cv2.imshow('Result', img)
cv2.waitKey(0)
