import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5) , 0)
cv2.imshow("Image", image)

lap=cv2.Laplacian(image , cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow("laplacian", lap)

soblX = cv2.Sobel(image ,cv2.CV_64F,1,0)
soblY = cv2.Sobel(image ,cv2.CV_64F,0,1)

soblX = np.uint8(np.absolute(soblX))
soblY = np.uint8(np.absolute(soblY))

sobelCombined = cv2.bitwise_or(soblX,soblY)

cv2.imshow("sX",soblX)
cv2.imshow("sY",soblY)
cv2.imshow("scb",sobelCombined)
(cnts, _)=cv2.findContours(sobelCombined.copy(),cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)

print("I count {} cubes".format(len(cnts)))

coins=image.copy()
cv2.drawContours(coins , cnts , -1 ,(0,255,0),2)
cv2.imshow("coins",coins)

cv2.waitKey(0)