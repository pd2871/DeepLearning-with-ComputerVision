from mtcnn.mtcnn import MTCNN
import cv2,os
import numpy as np
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

train = pd.read_csv("bbox_train.csv")

#print(len(set(train['Name'])))

unique_train_images = []
for img in (set(train['Name'])):
    unique_train_images.append(img)

#print(len(unique_train_images))

img_names = os.listdir("image_data")
img_dir = os.path.join("image_data")
#
# #print(len(img_names))
#
# test_images = set(img_names) - set(unique_train_images)
#
# #print(len(test_images))

test_set = pd.read_csv("test.csv")

#print(len(set(test_set["Name"])))
test_images=[]
for img in list(test_set["Name"]):
    test_images.append(img)

#print(len((test_images)))

mt = MTCNN()
bbox=[]
head_count=[]
test_imgs=[]
for img in test_images:
    test_imgs.append(img)

    image = os.path.join("image_data",img)
    image = cv2.imread(image)
    mtfaces = mt.detect_faces(image)

    for face in mtfaces:
        #print(face)
        x,y,w,h = face['box']
        x2 = x+w
        y2 = y+h
        #fc = image[y:y2, x:x2]
        bbox.append((x,y,x2,y2))

    head_count.append(len(bbox))

sub = pd.DataFrame({"Name": test_imgs, "HeadCount":head_count})
sub.to_csv("sub.csv", index=False)


# for bbox in bbox:
#     x,y,x2,y2 = bbox
#
#     cv2.rectangle(image, (x,y),(x2,y2),(255,0,0), 3)
#     cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

