import cv2


def capture(video, freq):
    vc = cv2.VideoCapture(video)  # 讀入視頻文件
    c = 1
    count = 0
    if vc.isOpened():  # 判斷是否正常打開
        rval, frame = vc.read()
    else:
        rval = False

    timeF = freq  # 視頻幀計數間隔頻率

    while rval:  # 循環讀取視頻幀
        rval, frame = vc.read()
        if (c % timeF == 0):  # 每隔timeF幀進行存儲操作
            cv2.imwrite('image/' + str(c) + '.jpg', frame)  # 存儲為圖像
            print('image/' + str(c) + '.jpg' + "  saved.")  # 存儲為圖像
            count = count + 1
        c = c + 1
        cv2.waitKey(1)
    print(count, " capture had been saved in image/.")
    vc.release()
