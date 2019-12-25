import cv2
import numpy as np
import argparse
from urllib import request as urllib
from .CodeConverter import CodeConverter
#import CodeConverter

class Feature_Extraction():

    def __init__(self):
        pass

    def classify_grid(self, image, x, y):
        height = np.size(image, 0)
        width = np.size(image, 1)
        row_size = height / 3.0
        column_size = width / 2.0

        for i in range(0, 2):
            for j in range(1, 4):
                if (y > row_size * (j - 1) and y < row_size * j and x > column_size * i and x < column_size * (i + 1)):
                    return i * 3 + j      

    # finds circles well
    def find_contours(self, image):
        #cv2.imshow('letter', image)
        #cv2.waitKey(0)
        #cv2.imwrite("original.jpg", image)
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.dilate(image, kernel, iterations=3)
        mask = cv2.erode(mask, kernel, iterations=6)
        mask = cv2.Canny(mask, 70, 200)
        #cv2.imwrite('edges.jpg', mask)

        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[0]
        contours.sort(key=lambda x:cv2.boundingRect(x)[0])
        
        array = []
        for c in contours:
            (x,y),r = cv2.minEnclosingCircle(c)
            center = (int(x),int(y))
            r = int(r)
            if r >=0 and r <= 15:
                cv2.circle(image, center, r, (0,255,0), 5)
                array.append(c)
        #cv2.imwrite("detected.jpg", image)

        encoding = list()
        for c in array:
            (x,y),r = cv2.minEnclosingCircle(c)
            center = (int(x), int(y))
            grid = self.classify_grid(image, center[0], center[1])
            if type(grid) == int:
                encoding.append(grid)
        encoding.sort()
        code = ''.join(str(x) for x in encoding)
        cc = CodeConverter()
        return cc.translate(code)


# im = cv2.imread("static/images/bubble.jpg")
# fe = Feature_Extraction()
# fe.find_contours(im)