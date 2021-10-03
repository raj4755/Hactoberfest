import cv2 as cv
import numpy as np

img = cv.imread('images/cat3.jpg')
cv.imshow('Cat', img)

# Averaging
average = cv.blur(img, (2,2))
cv.imshow("Average", average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (1,1), 0)
cv.imshow('Gaussian', gauss)

# median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral
bilat = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow("Bilateral", bilat)


cv.waitKey(0)