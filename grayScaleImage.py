import cv2
def grayScaleimage(img):
    grayscaleimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return grayscaleimg