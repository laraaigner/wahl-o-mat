import cv2
import numpy as np

img = cv2.imread(r"C:\Users\laraa\Desktop\wahlzettel.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img, (11, 11), 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
image = cv2.Canny(img, 100, 150)
#cv2.imshow("Image", img)
#cv2.imshow("Sobelx", sobelx)
#cv2.imshow("Sobely", sobely)
#cv2.imshow("Laplacian", laplacian)
cv2.imshow("Wahlzettel", image)
cv2.waitKey(0)
cv2.destroyAllWindows()