import cv2
import numpy as np
import pytesseract
from PIL import Image

def image_process(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask3 = np.full((image.shape[0], image.shape[1]), 0, dtype=np.uint8)
    # binary
    blur = cv2.GaussianBlur(gray,(3,3),0)
    ret3,mask3 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #for x in range(image.shape[0]):
    #    for y in range(image.shape[1]):
    #        if hsv[x][y][2] > 190:
    #            mask3[x][y] =255
    # Invert colors, black=white, white=black
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    mask3 = cv2.dilate(mask3, rect_kernel, iterations = 1)
    kernel = np.ones((5,5),np.uint8)
    mask3 = cv2.morphologyEx(mask3, cv2.MORPH_CLOSE, kernel)
    # Finding contours
    contours, hierarchy = cv2.findContours(mask3, cv2.RETR_TREE,
                                                    cv2.CHAIN_APPROX_SIMPLE)
    im2 = image.copy()
    orig_width = image.shape[0]
    orig_height = image.shape[1]

    min_cont_h = orig_height * 0.2
    min_cont_w = orig_width * 0.2
    
    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    text=[]
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w < min_cont_w or h < min_cont_h:
          continue
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = mask3[y:y + h, x:x + w]
    text.append(pytesseract.image_to_string(Image.fromarray(np.asarray(mask3)), config='--psm 10'))
    return text,cv2.cvtColor(mask3, cv2.COLOR_GRAY2BGR)