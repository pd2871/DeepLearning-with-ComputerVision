import cv2

#tracker = cv2.legacy_TrackerMOSSE.create()
tracker = cv2.TrackerCSRT_create()

cap = cv2.VideoCapture(0)

ret, img = cap.read()
bbox = cv2.selectROI("Tracker", img, False)
tracker.init(img,bbox)

def drawBox(frame, bbox):
    x, y ,w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(frame, (x,y),(x+w, y+h), (255,0,0), 3,1)
    cv2.putText(frame, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Frames", frame)

while True:

    success, img = cap.read()
    
    suc, bbox = tracker.update(img)
    if suc:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Not found", (75, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
