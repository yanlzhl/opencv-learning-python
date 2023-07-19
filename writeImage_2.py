import cv2

# name and size of window
cv2.namedWindow("test", cv2.WINDOW_NORMAL);
img = cv2.imread("/Users/neverland/Pictures/client.png")

# show img and get the event of keyboard
cv2.imshow("img",img)
key = cv2.waitKey(0)

if(key == 113):
    print("you had clicked the button Q")
    cv2.destroyWindow("test")
elif( key & 0xFF == ord('w')):
    print("you had clicked the button W, it will write a new image")
    cv2.imwrite("/Users/neverland/Pictures/client_1.png", img)
    cv2.destroyWindow("test")