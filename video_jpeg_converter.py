# File name: video_jpeg_converter.py
# Objective: To return a set of continuous JPEG images from an input video (useful for annotation of videos)

from imutils import paths
import cv2
import os

# Path for input videos (which will be converted to a series of JPEG images)
dataPath = str(input("Copy the path to your video input data and paste it here: "))

# Path for output JPEG images
outPath = str(input("Copy the path to your output folder storing the JPEG images and paste it here: "))

for classPath in os.listdir(dataPath):
    clipPaths = os.listdir(dataPath + "\\" + classPath)
    os.mkdir((outPath + '\\' + classPath))
    
    k = 1
    for clips in clipPaths:
        os.mkdir((outPath + '\\' + classPath + '\\' + clips))
        os.chdir((outPath + '\\' + classPath + '\\' + clips))
        
        f = dataPath + "\\" + classPath + "\\" + clips
        cam = cv2.VideoCapture(f)
        ret, frame = cam.read()
        currentframe = 0
        i = 0
        
        # a variable to set how many frames you want to skip
        frame_skip = 5          # Since the videos are in 30 FPS, and we want 10 frames per clip

        while cam.isOpened():
            ret, frame = cam.read()
            k += 1
            if not ret:
                break
            if (i > frame_skip - 1):
                cv2.imwrite(classPath + '_' + clips + '_' + str(k) +'.jpg', frame)
                i = 0
                continue
            i += 1

        cam.release()
        cv2.destroyAllWindows()