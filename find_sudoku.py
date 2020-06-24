import cv2
import numpy as np

def locate_board():
    image_path = 'images\image2.png'
    img= cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.medianBlur(img,5)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,4)
    cv2.imshow('image', img)
    cv2.waitKey(0)

if __name__=="__main__":
    locate_board()