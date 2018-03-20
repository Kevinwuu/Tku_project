# import numpy as np
import cv2
import imutils
from time import sleep, asctime

cap = cv2.VideoCapture("2.1M Full HD 1080P CCTV Footage.mp4")
s = cap.set(cv2.CAP_PROP_FPS, 10)
rate = cap.get(cv2.CAP_PROP_FPS)
total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
while(cap.isOpened()):

    # 得到當前影片的時間位置
    total_time = cap.get(cv2.CAP_PROP_POS_MSEC)
    print(total_time/1000)
    ret, frame = cap.read()

    # 必須加判斷,不然最後一禎會出問題
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = imutils.resize(gray, width=500)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
print("\n--------------------------------")
print("總共", total_frame, "frame")
print("每秒", rate, "禎")
print("影片長度", total_frame/rate, "s")

# 此方法會返回以下形式的24个字符的字符串： 'Tue Feb 17 23:21:05 2009'.
print("現在的時間是", asctime()[11:19])
cap.release()
cv2.destroyAllWindows()
