import numpy as np
import cv2
import os
import function
from PIL import Image

allfiles = os.listdir("image_folder/sample1")
imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]
count = 0
first_line = 1
line_len = 0
line_list = []
thresh = 20
similar = 0.07

while(True):
    if count == len(imlist)-1: 
        break
    sim_list = []
    keep_list = []
    frame1_list = []
    frame2_list = []
    bg = Image.open("image_folder/sample1/"+imlist[0])
    img1 = Image.open("image_folder/sample1/"+imlist[count])
    img2 = Image.open("image_folder/sample1/"+imlist[count+1])

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
 
    for a in range(len(areas1)):    
        if areas1[a] > 2000 and areas1[a] < 6000:
            x,y,w,h = cv2.boundingRect(contours1[a])
            if w*h < 9000:
                cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
                frame1_list.append((function.hist(img1[y:y+h,x:x+w,:]),((int)((2*x+w)/2),(int)((2*y+h)/2))))
                
    for a in range(len(areas2)):    
        if areas2[a] > 2000 and areas2[a] < 6000:
            x,y,w,h = cv2.boundingRect(contours2[a])
            if w*h < 9000:
                cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
                frame2_list.append((function.hist(img2[y:y+h,x:x+w,:]),((int)((2*x+w)/2),(int)((2*y+h)/2))))
            
    for i in range(len(frame1_list)):
        if len(frame1_list) == 0 or len(frame2_list) == 0: 
            break
        sim = 1
        sim_i = 0
        sim_j = 0
        for j in range(len(frame2_list)):
            norm = np.linalg.norm(frame1_list[i][0]-frame2_list[j][0])
            if sim > norm and norm < similar:
                sim = norm
                sim_i = i
                sim_j = j
        if np.linalg.norm(frame1_list[sim_i][0]-frame2_list[sim_j][0]) < similar:
            sim_list.append((sim_i,sim_j)) 
    
    for i in range(len(sim_list)):
        if len(sim_list) == 0:
            break      
        
        f1,f2 = (frame1_list[sim_list[i][0]][1],frame2_list[sim_list[i][1]][1])
        
        if sum(list(map(lambda x,y:(x-y)**2, f1,f2)))**(1/2) < 500:
            for j in range(len(line_list)):
                if frame1_list[sim_list[i][0]][1] == line_list[j][-1][1]:
                    line_list[j].append([f1,f2])
                    keep_list.append(j)
                    first_line = 0
                    break
                else:
                    first_line = 1
            if first_line:
                line_list.append([[f1,f2]])
                keep_list.append(len(line_list)-1)
            
    for i in range(len(keep_list)):
        for j in range(len(line_list[keep_list[i]])):
            cv2.line(img2,line_list[keep_list[i]][j][0],line_list[keep_list[i]][j][1],(0,255,0),5)
        
    cv2.imshow("frame",img2)
    count+=1
    if cv2.waitKey(1000) == 13:
        continue
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()