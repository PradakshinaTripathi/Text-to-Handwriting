import pywhatkit as kit

import cv2
m = input("Enter the text here... ")
kit.text_to_handwriting(m, save_to="handwriting.png")
image = cv2.imread("handwriting.png")
cv2.imshow("Converting your text to Handwritten text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

input()