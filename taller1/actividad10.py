import numpy as np
import matplotlib.pyplot as plt

rojo = "rojo.png"
verde = "verde.png"
azul = "azul.png"

rojo_img = plt.imread(rojo)
verde_img = plt.imread(verde)
azul_img = plt.imread(azul)

min_alto = min(rojo_img.shape[0], verde_img.shape[0], azul_img.shape[0])
min_ancho = min(rojo_img.shape[1], verde_img.shape[1], azul_img.shape[1])

rojo_img = rojo_img[:min_alto, :min_ancho]
verde_img = verde_img[:min_alto, :min_ancho]
azul_img = azul_img[:min_alto, :min_ancho]

original = rojo_img + verde_img + azul_img
original[:, :, 3] = 1.0


plt.subplot(1,4,1)
plt.imshow(rojo_img)
plt.axis('off')
plt.title("rojo")

plt.subplot(1,4,2)
plt.imshow(verde_img)
plt.axis('off')
plt.title("verde")

plt.subplot(1,4,3)
plt.imshow(azul_img)
plt.axis('off')
plt.title("azul")

plt.subplot(1,4,4)
plt.imshow(original)
plt.axis('off')
plt.title("original")


plt.figtext(0.09, 0.5, '(', fontsize=30, va='center')
plt.figtext(0.29, 0.5, ',', fontsize=30, va='center')
plt.figtext(0.50, 0.5, ',', fontsize=30, va='center')
plt.figtext(0.69, 0.5, ')', fontsize=30, va='center')
plt.figtext(0.704, 0.5, '=', fontsize=30, va='center')

plt.show()

