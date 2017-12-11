import cv2
import numpy as np
# from matplotlib import pyplot as plt

print("hello")
# 讀圖
image = cv2.imread("image/can.jpg")

# 轉灰階
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                              cv2.THRESH_BINARY_INV, 11, 2)

# 高斯慮波
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
# blurred = cv2.threshold(blurred, 0, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

# 肯尼邊緣偵測
binaryIMG = cv2.Canny(blurred, 50, 150)

# 找輪廓, cnts是個list,存放每組封閉輪廓的座標
(_, cnts, _) = cv2.findContours(binaryIMG.copy(),
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 創造clone用來畫圖
clone = image.copy()
cv2.namedWindow("image", cv2.WINDOW_KEEPRATIO)
cv2.imshow("image", gray)
# cv2.namedWindow("th", cv2.WINDOW_KEEPRATIO)
# cv2.imshow("th", blurred)
cv2.namedWindow("canny", cv2.WINDOW_KEEPRATIO)
cv2.imshow("canny", binaryIMG)
i = 0
for c in cnts:
    # print(c)

    # 利用moment得到中點
    M = cv2.moments(c)
    # print(M)
    if int(M["m00"]) == 0:
        cX = 0
        cY = 0
    else:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    # 計算面積
    area = cv2.contourArea(c)
    # perimeter = cv2.arcLength(c, True)    # 計算周長
    print(area)

    # 依Contours圖形建立mask
    mask = np.zeros(gray.shape, dtype="uint8")

    # 設定車子pixel範圍，將mask與原圖做bitwise得到物件
    if area > 1000.0:

        cv2.drawContours(mask, [c], -1, 255, -1)  # 255        →白色, -1→塗滿
        x, y, w, h = cv2.boundingRect(mask)
        cv2.namedWindow("Mask", cv2.WINDOW_KEEPRATIO)
        cv2.imshow("Mask", mask)
        i = i + 1

        # 將mask與原圖形作AND運算
        coins = cv2.bitwise_and(image, image, mask=mask)
        cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(clone, (cX, cY), 10, (1, 227, 254), -1)
        cv2.putText(clone, "#%d" % i, (x + int(w / 3), y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, (252, 197, 5), 3)
        # cv2.namedWindow("Image + Mask", cv2.WINDOW_KEEPRATIO)
        cv2.namedWindow("clone", cv2.WINDOW_KEEPRATIO)
        # cv2.imshow("Image + Mask", coins)
        cv2.imshow("clone", clone)
        # cv2.putText(clone, "#", (cX – 20, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.1,
        # (252, 197, 5), 3)
    cv2.waitKey(0)
# show the images


# for i in range(15, 18):
#     cv2.drawContours(clone, cnts, i, (0, 255, 0), 2)
#     cv2.namedWindow("clone", cv2.WINDOW_KEEPRATIO)
#     cv2.imshow("clone", clone)
#     cv2.waitKey(0)

# cv2.waitKey(0)

'''
for c in cnts:
    mask = np.zeros(gray.shape, dtype="uint8")  # 依Contours圖形建立mask
    cv2.drawContours(mask, [c], -1, 255, -1)  # 255        →白色, -1→塗滿
# show the images



    cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))

    cv2.waitKey(0)
'''
