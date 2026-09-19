import numpy as np
import matplotlib.pyplot as plt

matriz = np.zeros((3,3,3), dtype=np.uint8)

# blanco
matriz[0,1,0] = 255 ; matriz[0,1,1] = 255 ; matriz[0,1,2] = 255

#
matriz[1,0,0] = 255 ; matriz[1,0,1] = 0 ; matriz[1,0,2] = 255

# cian
matriz[0,0,0] = 135 ; matriz[0,0,1] = 206 ; matriz[0,0,2] = 235
# gris
matriz[1,1,0] = 128 ; matriz[1,1,1] = 128 ; matriz[1,1,2] = 128

# Amarillo
matriz[2,0,0] = 255 ; matriz[2,0,1] = 255 ; matriz[2,0,2] = 0

# rojo
matriz[0,2,0] = 255
# verde
matriz[1,2,1] = 255
# azul
matriz[2,2,2] = 255



plt.imshow(matriz)
plt.axis('off')
plt.title("Matriz colores")
plt.show()
