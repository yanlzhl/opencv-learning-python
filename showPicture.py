import cv2

# name and size of window
cv2.namedWindow("test", cv2.WINDOW_NORMAL);
img = cv2.imread("/Users/neverland/Pictures/client.png")

cv2.imshow("img",img)
key = cv2.waitKey(0)

# equal  the button Q, or ord('q') == key or key & 0xFF == ord('q').
# note, key & 0xFF in order to get last 8 digit of ASCII
if(key == 113):
    print("you had clicked the button Q")
    cv2.destroyWindow("test")
    # exit()

cv2.destroyWindow("test")
# cv2.destroyAllWindows()