import numpy as np
import matplotlib.pyplot as plt

ruta = "colores.png"
G = plt.imread(ruta)



gris = ((G[:, :, 0] + G[:, :, 1] + G[:, :, 2]) / 3)


plt.subplot(1,2,1)
plt.imshow(G)
plt.axis('off')
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(gris, cmap="gray")
plt.axis('off')
plt.title("gris average")
plt.show()