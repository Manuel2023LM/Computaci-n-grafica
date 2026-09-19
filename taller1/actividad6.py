import numpy as np
import matplotlib.pyplot as plt

dado = "image23.png"
img = plt.imread(dado)

azul = np.copy(img)
azul[:,:,0] = 0
azul[:,:,1] = 0

plt.subplot(1,2,1)
plt.imshow(img)
plt.axis('off')
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(azul)
plt.axis('off')
plt.title("canal azul")
plt.show()

