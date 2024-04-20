import cv2
img = cv2.imread("rgb.webp")
cv2.imshow("Imagem de Exibicao", img)
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Escala de Cinza", gray_img)
print(img)
cv2.waitKey(0)