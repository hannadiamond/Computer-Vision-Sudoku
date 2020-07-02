import cv2
import imutils
import numpy as np

def locate_board(): 
    image_path = 'images\image2.png'
    orig_img = img= cv2.imread(image_path)
    img= cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_size = img.shape
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,51,4)
    cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    squares = find_squares(cnts, img_size)
    for c in squares:
        cv2.drawContours(orig_img, [c], -1, (0, 255, 0), 2)
    cv2.imshow('image', orig_img)
    cv2.waitKey(0)

def find_squares(cnts, img_size):
    img_area = img_size[0]*img_size[1]
    squares = []
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape_area = w*h
            shape_percentage = shape_area/img_area
            if 0.95 <= ar <= 1.05 and 0.20 <= shape_percentage < 0.90:
                squares.append(c)
    return squares

if __name__=="__main__":
    locate_board()