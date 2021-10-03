import cv2 as cv
import numpy as np

img = cv.imread('images/cat4.jpg')
# cv.imshow('Cat', img)

blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# Changing Color to Green
blank[:] = 0,255,0
cv.imshow('Green', blank)

# Changing Color to Red
blank[:] = 0,0,255
cv.imshow('Red', blank)

# Changing a part to Red
blank[50:50, 100:100] = 0,0,255
cv.imshow('PartRed', blank)


# 1. DRAWIG A RECTANGLE
cv.rectangle(blank, (10,10), (150, 150), (0,255,0), thickness=2)
# cv.rectangle(blank, (10,10), (150, 150), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 2. DRAWIG A CIRCLE
cv.circle(blank, (250, 250), 100, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# 3. DRAWIG A Line
cv.line(blank, (100,150), (200, 150), (0, 0, 255), thickness=2)
cv.imshow('Line', blank)

# WRITE TEXT ON IMAGE
cv.putText(blank, 'this is text', (250, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('Text', blank)



cv.waitKey(0)