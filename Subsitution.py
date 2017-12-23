import cv2
from matplotlib import pyplot as plt
import numpy as np


# 讀圖
bg = cv2.imread("image/00.jpg", 0)
origin = cv2.imread("image/01.jpg")
img2 = origin.copy()


# 原圖轉灰階
gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
# 讀長寬
row, col, depth = origin.shape
print(origin.shape)

gray = gray - bg

gray = cv2.medianBlur(gray, 5)

# 二值化
ret, th = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
kernel = np.ones((11, 11), np.uint8)
open = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
close = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
blur = cv2.medianBlur(open, 5)

# 畫外接矩形，將原圖物件框起來
x, y, w, h = cv2.boundingRect(open)
cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 3)

# 畫當前旋轉角度的舉行
# contour找邊緣點座標
im2, contours, hierarchy = cv2.findContours(
    th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
# print(cnt)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img2, [box], 0, (0, 0, 255), 3)

# #擷取車子
imcrop = img2[y:y + h, x:x + w]
cv2.namedWindow("crop", cv2.WINDOW_KEEPRATIO)
cv2.imshow("crop", imcrop)


# # 個別視窗顯示
# cv2.namedWindow("origin", cv2.WINDOW_KEEPRATIO)
# cv2.namedWindow("substract", cv2.WINDOW_NORMAL)
# cv2.namedWindow("th", cv2.WINDOW_NORMAL)
# cv2.namedWindow("open", cv2.WINDOW_NORMAL)
# cv2.namedWindow("blur", cv2.WINDOW_NORMAL)
# # cv2.namedWindow("close", cv2.WINDOW_NORMAL)


# cv2.imshow("origin", origin)
# cv2.imshow("substract", gray)
# cv2.imshow("th", th)
# cv2.imshow("open", open)
# cv2.imshow("blur", blur)
# print(blur.shape)
# # cv2.imshow("close", close)



# plt會倒過來顯示色彩，所以要調整
plt.subplot(241), plt.imshow(cv2.cvtColor(
    origin, cv2.COLOR_BGR2RGB), "gray"), plt.title('Origin')
plt.axis('off')
plt.subplot(242), plt.imshow(gray, 'gray'), plt.title('Gray')
plt.axis('off')
plt.subplot(243), plt.imshow(blur, "gray"), plt.title('Blur')
plt.axis('off')
plt.subplot(244), plt.imshow(th, 'gray'), plt.title('Th')
plt.axis('off')
plt.subplot(245), plt.imshow(cv2.cvtColor(
    img2, cv2.COLOR_BGR2RGB), "gray"), plt.title('Plot')
plt.axis('off')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
