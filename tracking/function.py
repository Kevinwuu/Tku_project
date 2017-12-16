import numpy as np

def hist(img):
    bin = 50
    imgArr = np.array(img,dtype=np.float)

    imgArr_R = imgArr[:,:,0].ravel()
    h_r = np.histogram(imgArr_R,bin,range=(0,255))

    imgArr_G = imgArr[:,:,1].ravel()
    h_g = np.histogram(imgArr_G,bin,range=(0,255))

    imgArr_B = imgArr[:,:,2].ravel()
    h_b = np.histogram(imgArr_B,bin,range=(0,255))

    all_h_y = []
    all_h_y.append(h_r[0])    
    all_h_y.append(h_g[0])
    all_h_y.append(h_b[0])

    all_h_y_Arr = np.array(all_h_y,dtype=np.float).ravel()
    all_h_y_Arr = all_h_y_Arr/np.sum(all_h_y_Arr)
    return all_h_y_Arr

