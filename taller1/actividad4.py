import numpy as np
import matplotlib.pyplot as plt

dado = "image23.png"
img = plt.imread(dado)

rojo = np.copy(img)
rojo[:,:,1] = 0
rojo[:,:,2] = 0

plt.subplot(1,2,1)
plt.imshow(img)
plt.axis('off')
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(rojo)
plt.axis('off')
plt.title("canal rojo")
plt.show()