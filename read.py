import cv2 as cv


# IMAGE READING
img  = cv.imread('images/cat_large.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)


# READING VIDEOS

capture = cv.VideoCapture('videos/VID-20201215-WA0112.mp4')

while True:
    istrue, frame = capture.read()

    cv.imshow('Videos', frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break


capture.release()
capture.destroyAllWindows()


