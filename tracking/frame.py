import numpy as np
import cv2
import os
import function as fc
from PIL import Image

folder = "image_folder/sample1/"
allfiles = os.listdir(folder)
imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]
count = 0
line_list = []
thresh = 20

while(True):
    if count == len(imlist)-1: 
        break
    sim_list = []
    keep_list = []
    frame1_list = []
    frame2_list = []
    bg = Image.open(folder+imlist[0])
    img1 = Image.open(folder+imlist[count])
    img2 = Image.open(folder+imlist[count+1])

    img_w,img_h = bg.size
    width = 500
    height = (int)((width/img_w)*img_h)
    bg = bg.resize((width,height),Image.BILINEAR)
    img1 = img1.resize((width,height),Image.BILINEAR)
    img2 = img2.resize((width,height),Image.BILINEAR)

    bg = np.array(bg)
    img1 = np.array(img1)
    img2 = np.array(img2)

    bg = cv2.cvtColor(bg, cv2.COLOR_RGB2BGR)
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
    img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)

    bg_grey = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    grey1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    grey2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    bg_blur = cv2.GaussianBlur(bg_grey,(7,7),0)
    blur1 = cv2.GaussianBlur(grey1,(7,7),0)
    blur2 = cv2.GaussianBlur(grey2,(7,7),0)
    
    d1 = cv2.absdiff(blur1, bg_blur)
    d2 = cv2.absdiff(blur2, bg_blur)

    th1 = cv2.threshold( d1, thresh, 255, cv2.THRESH_BINARY )[1]
    th2 = cv2.threshold( d2, thresh, 255, cv2.THRESH_BINARY )[1] 
   
    kernel = np.ones((3,3), np.uint8)

    dilated1 = cv2.dilate(th1, kernel, iterations=1)
    dilated2 = cv2.dilate(th2, kernel, iterations=1)
    
    contours1 = cv2.findContours(dilated1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[1]
    contours2 = cv2.findContours(dilated2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[1]

    areas1 = [cv2.contourArea(c) for c in contours1]
    areas2 = [cv2.contourArea(c) for c in contours2]   
 
    fc.find_center_and_hist(frame1_list,areas1,contours1,img1)
    fc.find_center_and_hist(frame2_list,areas2,contours2,img2)
            
    fc.find_sim(sim_list,frame1_list,frame2_list,0.07)
    
    fc.find_trace(line_list,keep_list,frame1_list,frame2_list,sim_list)    
            
    fc.draw_trace(img2,line_list,keep_list)
        
    cv2.imshow("frame",img2)
    count+=1
    if cv2.waitKey(1000) == 13:
        continue
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()