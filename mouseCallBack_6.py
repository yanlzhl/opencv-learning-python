import cv2
import numpy as np

# self-defined method to display the information
def mouse_callback(event, x, y, flags,message):
    print(event, x, y, flags,message)

# name and size of window
cv2.namedWindow("test", cv2.WINDOW_NORMAL);
cv2.resizeWindow("test",640, 360)
cv2.setWindowTitle("test", "test")

# mouseCallBack
cv2.setMouseCallback("mouse", mouse_callback, "this is a message")

#define a image
img = np.zeros((360, 640, 3), np.uint8)
while True:
    cv2.imshow("image", img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cv2.destroyWindow("test")

