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
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    text.append(pytesseract.image_to_string(Image.fromarray(np.asarray(mask3)), config='--psm 10'))
    return text,cv2.cvtColor(mask3, cv2.COLOR_GRAY2BGR)

def object_detect(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue ,saturation ,value = cv2.split(hsv)
    mask3 = np.full((image.shape[0], image.shape[1]), 0, dtype=np.uint8)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if hsv[x][y][2] > 170:
                mask3[x][y] =255
    # Invert colors, black=white, white=black
    #rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    #mask3 = cv2.dilate(mask3, rect_kernel, iterations = 1)
    kernel = np.ones((5,5),np.uint8)
    mask3 = cv2.morphologyEx(mask3, cv2.MORPH_CLOSE, kernel)
    # Finding contours
    retval, thresholded = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    medianFiltered = cv2.medianBlur(thresholded,5)
    mask3 = medianFiltered
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
    cop_img = image.copy()
    cop_image2 = mask3.copy()
    cop_image2 = cv2.cvtColor(cop_image2, cv2.COLOR_GRAY2BGR)
    shape=''
    for c in contours:
      rot_rect = cv2.minAreaRect(c)
      _,size,_ = rot_rect
      area = size[0]*size[1]
      if area < min_cont_h*min_cont_w:
         continue
      box = cv2.boxPoints(rot_rect)
      box = np.int0(box)
      peri = cv2.arcLength(c, True)
      approx = cv2.approxPolyDP(c, 0.04 * peri, True)
      print(len(approx))
      if len(approx) == 3:
        shape = "triangle"
      # if the shape has 4 vertices, it is either a square or
      # a rectangle
      elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
        hape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
		# if the shape is a pentagon, it will have 5 vertices
      elif len(approx) == 5:
        shape = "pentagon"
      # otherwise, we assume the shape is a circle
      else:
        shape = "circle"
    
      cv2.drawContours(cop_img,[c],0,(0,0,0),2)
      # get rotated rectangle from contour
      
      # draw rotated rectangle on copy of img
      text = str(len(approx))
      text_font = cv2.FONT_HERSHEY_SIMPLEX
      text_scale = 0.8
      text_color = (255, 255, 255)
      text_thickness = 1

      # Calculate the position for the text
      text_size = cv2.getTextSize(text, text_font, text_scale, text_thickness)[0]
      text_position = (box[0] - text_size[0], box[1] + text_size[1])

      # Write the text on the image
      #cv2.putText(image, text, text_position, text_font, text_scale, text_color, text_thickness, cv2.LINE_AA)

      cv2.drawContours(cop_image2,[box],0,(0,255,0),2)
      break
    return shape,cop_image2