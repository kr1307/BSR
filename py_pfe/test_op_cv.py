from __future__ import print_function
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5) , 0)

cv2.imshow("Image", image)

thresh = cv2.adaptiveThreshold(blurred,255,
cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("thresh_1", thresh)

thresh = cv2.adaptiveThreshold(blurred,255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("thresh_2", thresh)

cv2.waitKey(0)