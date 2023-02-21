import cv2
import argparse
import numpy as np

# Charger l'image
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])


# Convert the image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a window to display the image
cv2.namedWindow("Image")

# Create a trackbar to change the values of the lower and upper range
def nothing(x):
    pass
cv2.createTrackbar("LowerH", "Image", 0, 180, nothing)
cv2.createTrackbar("LowerS", "Image", 0, 255, nothing)
cv2.createTrackbar("LowerV", "Image", 0, 255, nothing)
cv2.createTrackbar("UpperH", "Image", 180, 180, nothing)
cv2.createTrackbar("UpperS", "Image", 255, 255, nothing)
cv2.createTrackbar("UpperV", "Image", 255, 255, nothing)

# Display the image and trackbars until the user presses 'q'
while True:
    # Get the values of the lower and upper range from the trackbars
    lowerH = cv2.getTrackbarPos("LowerH", "Image")
    lowerS = cv2.getTrackbarPos("LowerS", "Image")
    lowerV = cv2.getTrackbarPos("LowerV", "Image")
    upperH = cv2.getTrackbarPos("UpperH", "Image")
    upperS = cv2.getTrackbarPos("UpperS", "Image")
    upperV = cv2.getTrackbarPos("UpperV", "Image")
    lower_range = np.array([lowerH, lowerS, lowerV])
    upper_range = np.array([upperH, upperS, upperV])
    
    # Threshold the image to get only the desired color
    mask = cv2.inRange(hsv, lower_range, upper_range)
    
    # Bitwise-AND the image and the mask to get only the desired color
    res = cv2.bitwise_and(img,img, mask= mask)
    
    # Display the resulting image
    cv2.imshow("Image", res)
    
    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy all windows
cv2.destroyAllWindows()