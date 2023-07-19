import cv2

# name and size of window
cv2.namedWindow("test", cv2.WINDOW_NORMAL);

# read frame of video
capture = cv2.VideoCapture("/Users/neverland/Pictures/202304171621_037425AA.MP4")

while True:
    ret, frame = capture.read() # ret value are true or false.
    cv2.imshow("video", frame)

    if(cv2.waitKey(40) == ord('q')): # the number of waitKey(40) means delay of time
        break

cv2.destroyWindow("test")
capture.release()

