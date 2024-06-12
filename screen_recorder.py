from PIL import ImageGrab
import cv2
import numpy as np
image = ImageGrab.grab(bbox=None,all_screens=True)
imcv = cv2.cvtColor(np.asarray(image),cv2.COLOR_BGR2RGB)
h,w,l = imcv.shape
size = (w,h)
recording = cv2.VideoWriter('project1.avi',cv2.VideoWriter_fourcc(*'DIVX'),15,size)
import time
timeout = time.time()+20
while True:
    if time.time()>timeout:
        break
    image = ImageGrab.grab(bbox=None, all_screens=True)
    imcv = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2RGB)
    recording.write(imcv)
recording.release()