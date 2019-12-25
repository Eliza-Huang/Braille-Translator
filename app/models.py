# models.py
# splits an image into its individual letters

import cv2
from .feature_extraction import Feature_Extraction
#import feature_extraction

LETTER_HEIGHT = 106
LETTER_WIDTH = 75
SPACING = 0

fe = Feature_Extraction()


def splitImage(fileName):
    img = cv2.imread(fileName, cv2.IMREAD_COLOR)

    height, width, channels = img.shape

    imgs = []

    y1 = 0
    y2 = LETTER_HEIGHT
    while (y2 <= height):
        x1 = 0
        x2 = LETTER_WIDTH
        while (x2 <= width):
            crop_img = img[y1:y2, x1:x2]
            #crop_img = crop_img.resize(crop_img, (60, 80))
            #crop_img = cv2.resize(crop_img, (60,80))
            imgs.append(crop_img.copy())
            x1 = x1 + (LETTER_WIDTH + SPACING)
            x2 = x2 + (LETTER_WIDTH + SPACING)
        y1 += (LETTER_HEIGHT + SPACING)
        y2 += (LETTER_HEIGHT + SPACING)
        
    sentence = ""
    for i in imgs:
        sentence += fe.find_contours(i)

    return sentence
