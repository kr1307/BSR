import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
grey = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5) , 0)
cv2.imshow("image", image)
cv2.imshow("blur", blurred)

edged = cv2.Canny(image,45,75)
cv2.imshow("edged",edged)

(contours, _)=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)


# Initialiser un compteur pour le nombre de rectangles
rectangle_count = 0

# boucle sur chaque contour
for contour in contours:
    # calculer l'aire du contour
    area = cv2.contourArea(contour)
    
    # vérifier si l'aire est comprise entre les limites
    if 100 < area :
        # dessiner un rectangle autour de chaque contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Incrémenter le compteur de rectangles
        rectangle_count += 1

# afficher le nombre de contours
print("Nombre de cubes :", rectangle_count)

# afficher l'image avec les rectangles
cv2.imshow("Resultat", image)
cv2.waitKey(0)
cv2.destroyAllWindows()