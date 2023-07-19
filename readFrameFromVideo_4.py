import cv2

# name and size of window
cv2.namedWindow("test", cv2.WINDOW_NORMAL);

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read() # ret value are true or false.
    cv2.imshow("front camera image", frame)

    if(cv2.waitKey(0) == ord('q')):
        break

cv2.destroyWindow("test")
capture.release()

