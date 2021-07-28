import os, cv2, time
import numpy as np

jungle = cv2.imread('jungle.png')
jungle = cv2.resize(jungle, (600,400))
jungle = cv2.GaussianBlur(jungle, (3,3), 9)

#creating trackbars to get values for HSV mask
# cv2.namedWindow("Trackbar")
# cv2.resizeWindow('Trackbar',400,400)

# def nothing(x):
#     pass
# cv2.createTrackbar('l_h','Trackbar', 0, 179, nothing)
# cv2.createTrackbar('l_s','Trackbar', 0, 255, nothing)
# cv2.createTrackbar('l_v','Trackbar', 0, 255, nothing)
# cv2.createTrackbar('u_h','Trackbar', 0, 179, nothing)
# cv2.createTrackbar('u_s','Trackbar', 0, 255, nothing)
# cv2.createTrackbar('u_v','Trackbar', 0, 255, nothing)

cap = cv2.VideoCapture('TigerGreenScreen.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (600,400))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # l_h = cv2.getTrackbarPos('l_h','Trackbar')
    # l_s = cv2.getTrackbarPos('l_s','Trackbar')
    # l_v = cv2.getTrackbarPos('l_v','Trackbar')
    # u_h = cv2.getTrackbarPos('u_h','Trackbar')
    # u_s = cv2.getTrackbarPos('u_s','Trackbar')
    # u_v = cv2.getTrackbarPos('u_v','Trackbar')

    # lower_bound = np.array([l_h, l_s, l_v])
    # upper_bound = np.array([u_h, u_s, u_v])

    #From trackbars
    lower_bound = np.array([35, 51,51])
    upper_bound = np.array([140, 255,255])
    mask = cv2.inRange(hsv, lowerb=lower_bound, upperb=upper_bound)
    frame_new = cv2.bitwise_and(frame, frame, mask=mask)
    back_sub = frame-frame_new

    final_image = np.where(back_sub==0, jungle, back_sub)
    #cv2.imshow("BACK", back_sub)
    #cv2.imshow("Frame", frame)
    # cv2.imshow("Final Image", final_image)
    # cv2.imshow("Original Image", frame)
    final = np.hstack([frame, final_image])
    cv2.imshow("Original Vs Final", final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()