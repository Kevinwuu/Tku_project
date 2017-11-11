from skimage.filters import threshold_adaptive
import numpy as np


import cv2
cap = cv2.VideoCapture("2.1M Full HD 1080P CCTV Footage.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((11, 11), np.uint8)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # 上下,左右
    road = frame[200:1200, 300:900]
    fgmask = fgbg.apply(road)

    fgmask = cv2.GaussianBlur(fgmask, (5, 5), 0)
    ret, fgmask = cv2.threshold(fgmask, 120, 255, cv2.THRESH_BINARY)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    car = cv2.bitwise_and(road, road, mask=fgmask)
    # inverse車輛的遮罩
    fgmask_inv = cv2.bitwise_not(fgmask)

    # 用白色當背景
    white = road.copy()
    white[:, :] = 255

    # 白色背景減去車輛遮罩，變成黑色車子在白色背景移動
    road_withoutCar = cv2.bitwise_and(white, white, mask=fgmask_inv)

    # [黑色車子在白色背景]+[真實車輛的影像]
    whiteroad_car = cv2.add(road_withoutCar, car)
    # 取得車子的輪廓
    image, contours, hierarchy = cv2.findContours(
        fgmask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 用線在車子輪廓上描出外框
    # car_contour1 = road.copy()
    # car_contour1 = cv2.drawContours(
    #     frame, contours, -1, (0, 255, 0), 3)

    # car_contour2 = road.copy()
    # car_contour3 = road.copy()
    # car_contour4 = road.copy()

    # car1 = road.copy()

    # fgmask_inv = cv2.bitwise_not(fgmask)

    # fgmask = cv2.fastNlMeansDenoisingColored(fgmask, None, 10, 10, 7, 21)

    # fgmask = cv2.medianBlur(fgmask, 3)
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)
    cv2.namedWindow('road', cv2.WINDOW_NORMAL)
    cv2.namedWindow('car', cv2.WINDOW_NORMAL)

    cv2.imshow('frame', frame)
    cv2.imshow('frame1', fgmask)
    cv2.imshow('road', road)
    cv2.imshow('car', road_withoutCar)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
