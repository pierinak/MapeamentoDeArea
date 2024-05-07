import cv2
import numpy as np

# Carregue a imagem
image1 = cv2.imread('antes.jpg')
image2 = cv2.imread('depois.jpg')



# Defina o intervalo de cores para verde
lower_green = np.array([30, 100, 30])
upper_green = np.array([85, 255, 255])

# Converta a imagem para o espaço de cores HSV
hsv1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

# Crie uma máscara que seleciona apenas os pixels verdes
mask1 = cv2.inRange(hsv1, lower_green, upper_green)
mask2 = cv2.inRange(hsv2, lower_green, upper_green)
# Crie uma imagem em branco do mesmo tamanho que a imagem original
white_image1 = np.ones_like(image1) * 255
white_image2 = np.ones_like(image2) * 255

# Use a máscara para definir os pixels verdes na imagem original para branco
result1 = cv2.bitwise_and(white_image1, white_image1, mask=mask1)
result2 = cv2.bitwise_and(white_image2, white_image2, mask=mask2)

# Converta os pixels não verdes para preto
result1[mask1==0] = 0
result2[mask2==0] = 0
# Salve a imagem resultante
cv2.imwrite('antes.png', result1)
cv2.imwrite('depois.png', result2)


area1_pixel = np.sum(result1 == 255)
area2_pixel = np.sum(result2 == 255)

area1_cm2 = round (area1_pixel / (128.8 **2), 2)
area2_cm2 = round (area2_pixel / (128.8 **2), 2)


print(f'A área da folha antes da herbivoria é {area1_cm2} cm²')
print(f'A área da folha depois da herbivoria é {area2_cm2} cm²')


#a distancia em pixels convertidos para cm é de 128.8
#distância em pixels 644.04
