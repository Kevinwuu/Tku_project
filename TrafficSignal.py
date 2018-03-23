# try:
#     # for Python2
#     from Tkinter import *
# except ImportError:
#     # for Python3
#     from tkinter import *
import tkinter as tk
from time import sleep


# 創建窗口
win = tk.Tk()
win.title('TrafficSignal')
win.geometry('300x350')

# 燈號標籤區塊
r = tk.Label(win, bg='white', font=('Arial, 12'),
             borderwidth=2, relief="solid", width=5, height=3)
r.place(x=70, y=40)
y = tk.Label(win, bg='white', font=('Arial, 12'),
             borderwidth=2, relief="solid", width=5, height=3)
y.place(x=130, y=40)
g = tk.Label(win, bg='green', font=('Arial, 12'),
             borderwidth=2, relief="solid", width=5, height=3)
g.place(x=190, y=40)


# 預設變數值
signal = True
result = tk.StringVar()
time = tk.StringVar()
time.set("0")
result.set("True")


def getSignal(x):

    print(x)


def count_time(i, j):
    while i >= 0 or j >= 0:
        time.set(i)
        print(i)
        win.update()
        sleep(1)
        i = i - 1
        if i == -1:
            change_light(1)
            # sleep(1)
            i = j
            j = -1


def change_light(FLAG):
    global signal
    global x

    # 紅燈時
    if signal is False:
        signal = True
        result.set("True")
        g.config(bg="green")
        r.config(bg="white")
    # 綠燈時
    else:
        signal = False
        g.config(bg="white")

        # 是否轉黃燈
        if FLAG:
            y.config(bg="yellow")
            win.update()
            sleep(2)
            y.config(bg="white")

        r.config(bg="red")
        result.set("False")

    getSignal(signal)


def test():
    print("Hello")


# 倒數計時
t = tk.Label(win, bg='black', textvariable=time, fg="white",
             font=('Arial, 10'), width=5, height=3)
t.place(x=245, y=45)


# 按鈕
s = tk.Button(win, text="Start", width=15, height=2,
              command=lambda: count_time(i=3, j=4))
s.place(x=100, y=120)

# p = tk.Button(win, text="Pause", width=15, height=2,
#               command=lambda: count_time(i=-1, j=-1))
p = tk.Button(win, text="Pause", width=15, height=2,
              command=test)

p.place(x=100, y=170)

c = tk.Button(win, text="Quick Change", cursor="target",
              width=15, height=2,
              command=lambda: change_light(FLAG=0))
c.place(x=100, y=220)




# 顯示狀態
show = tk.Label(win, textvariable=result,
                font=('Arial, 12'), width=10, height=2)
show.place(x=110, y=280)

win.mainloop()
