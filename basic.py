import cv2 as cv

img = cv.imread('images/cat3.jpg')
cv.imshow('Cat', img)

# Converting into greyscale

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

# Blur an Image

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# Edge Cascade

canny = cv.Canny(blur, 110, 120)
cv.imshow("Canny Edges", canny)

# Dilate Image

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# Erode Image
erode = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("Eroded", erode)

# Resize 

resize = cv.resize(img, (500, 500))
cv.imshow("Resized", resize)

# Crop

crop = img[100:150, 100:150]
cv.imshow('Cropped', crop)

cv.waitKey(0)