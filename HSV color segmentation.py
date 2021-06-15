import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbar")

def nothing(x):
    pass

#Trackbars create bars for a value selection from range of values
tb_lh = cv2.createTrackbar('tb_lh', 'Trackbar', 0, 179, nothing) #lower H (max value is 179)
tb_ls = cv2.createTrackbar('tb_ls', 'Trackbar', 0, 255, nothing) #lower S
tb_lv = cv2.createTrackbar('tb_lv', 'Trackbar', 0, 255, nothing) #lower V
tb_uh = cv2.createTrackbar('tb_uh', 'Trackbar', 0, 179, nothing) #upper H
tb_us = cv2.createTrackbar('tb_us', 'Trackbar', 0, 255, nothing) #upper S
tb_uv = cv2.createTrackbar('tb_uv', 'Trackbar', 0, 255, nothing) #upper V

while True:
    success, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('tb_lh', 'Trackbar')
    ls = cv2.getTrackbarPos('tb_ls', 'Trackbar')
    lv = cv2.getTrackbarPos('tb_lv', 'Trackbar')
    uh = cv2.getTrackbarPos('tb_uh', 'Trackbar')
    us = cv2.getTrackbarPos('tb_us', 'Trackbar')
    uv = cv2.getTrackbarPos('tb_uv', 'Trackbar')

    lower_hsv = np.array([lh,ls,lv])  #array containing low HSV values
    upper_hsv = np.array([uh,us,uv]) #array containing max HSV values

    """
    cv2.inRange will create mask (black and white image) just like cv2.threshold
    It takes three arguments, first one is frame, second one is the lower value of arrays
    If anything lower than these values appear in frame then it will be black 
    Else white
    """
    mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Result", res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()