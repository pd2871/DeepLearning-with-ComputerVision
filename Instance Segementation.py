import cv2

#Pixellib is important library for Instance and Semantic segmentation
from pixellib.instance import instance_segmentation
from pixellib.semantic import semantic_segmentation

ins_seg = instance_segmentation()  #For instance segementation
sem_seg = semantic_segmentation()  #For semantic segementation

ins_seg.load_model('mask_rcnn_coco.h5')
#sem_seg.model('mask_rcnn_coco.h5')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        result = ins_seg.segmentFrame(frame, show_bboxes=True)
        #result = sem_seg.segmentFrameAsPascalvoc(frame)

        #result is tuple containing dict in 0 index and image in 1 index
        image = result[1]

        cv2.imshow("Instance", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()




