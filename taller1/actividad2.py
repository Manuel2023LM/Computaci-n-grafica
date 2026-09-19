import numpy as np
import matplotlib.pyplot as plt

matriz = np.zeros((7,11,3), dtype=np.uint8)


# Amarillo
matriz[:5,0,0] = 255 ; matriz[:5,0,1] = 255 ; matriz[:5,0,2] = 0

# cian
matriz[:5,1:3,0] = 70 ; matriz[:5,1:3,1] = 200 ; matriz[:5,1:3,2] = 255

# magenta
matriz[0:5,5:7,0] = 255 ; matriz[0:5,5:7,1] = 0 ; matriz[0:5,5:7,2] = 255


'''
# blanco
matriz[0,1,0] = 255 ; matriz[0,1,1] = 255 ; matriz[0,1,2] = 255




# gris
matriz[1,1,0] = 128 ; matriz[1,1,1] = 128 ; matriz[1,1,2] = 128

'''

lista = np.linspace(0,255,11, dtype=np.uint8)
print(lista)

for i in range(11):
    matriz[5:7,i,:] = lista[i]


# rojo
matriz[:5,7:9,0] = 255

# verde

matriz[:5,3:5,1] = 255

# azul
matriz[:5,9:11,2] = 255




plt.imshow(matriz)
plt.axis('off')
plt.title("Matriz colores")
plt.show()
