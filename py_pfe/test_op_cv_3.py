import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
threshold_value, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Cont1", binary_image)

thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Cont", thresh)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} cubes".format(len(contours)))

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)


cv2.imshow("Contours", image)
cv2.waitKey(0)

