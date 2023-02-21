import cv2
import argparse
import numpy as np

# Charger l'image
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

# convertir l'image en espaces de couleur HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# définir les limites inférieures et supérieures de la plage de couleur
lower_color = np.array([0, 70, 105])
upper_color = np.array([180, 98, 255])

# masquer les couleurs en dehors de la plage de couleur
mask = cv2.inRange(hsv, lower_color, upper_color)

# trouver les contours dans l'image masquée
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# définir la taille minimale et maximale de l'aire
min_area = 300

# Initialiser un compteur pour le nombre de rectangles
rectangle_count = 0

# boucle sur chaque contour
for contour in contours:
    # calculer l'aire du contour
    area = cv2.contourArea(contour)
    
    # vérifier si l'aire est comprise entre les limites
    if min_area < area :
        # dessiner un rectangle autour de chaque contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Incrémenter le compteur de rectangles
        rectangle_count += 1

# afficher le nombre de contours
print("Nombre de cubes :", rectangle_count)

# afficher l'image avec les rectangles
cv2.imshow("Resultat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
