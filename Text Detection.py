import cv2, pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('images.png')

#pytesseract only accepts RGB, so convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
heightImg,widthImg,_ = img.shape

#displaying the texts from images
#print(pytesseract.image_to_string(img))

#displaying the bbox of detected characters
# boxes = pytesseract.image_to_boxes(img) #returns a single string consisting of all bounding boxes of characters
# for line in boxes.splitlines():
#     x, y, w, h = int(line.split()[1]), int(line.split()[2]), int(line.split()[3]), int(line.split()[4])
#     cv2.rectangle(img, (x,heightImg-y), (w, heightImg-h), (0,255,0), 2)
#     cv2.putText(img, line.split()[0], (x,heightImg-y+25), cv2.FONT_HERSHEY_SIMPLEX,1, (255,0,0), 2)


#displaying the bbox of detected words
boxes = pytesseract.image_to_data(img) #returns a single string consisting of all bounding boxes of words

for i, line in enumerate(boxes.splitlines()):
    #gives 10 columns having different values
    if i != 0 and len(line.split()) == 12: #escaping the first header and printing only valid rows
        x, y, w, h = int(line.split()[6]), int(line.split()[7]), int(line.split()[8]), int(line.split()[9])
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(img, line.split()[-1], (x,y+100), cv2.FONT_HERSHEY_SIMPLEX,1, (255,0,0), 2)

    
cv2.imshow("Image", img)

cv2.waitKey(0)




