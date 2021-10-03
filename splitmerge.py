import cv2 as cv
import numpy as np

img = cv.imread('images/cat3.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank", blank)


b, g, r = cv.split(img)


cv.imshow('Blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

blue = cv.merge([b, blank, blank])
green = cv.merge([ blank, g, blank])
red = cv.merge([blank, blank, r])
merge = cv.merge([b, g, r])

cv.imshow('Merged', merge)

cv.waitKey(0)