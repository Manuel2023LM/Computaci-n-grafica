import numpy as np
import matplotlib.pyplot as plt

dado = "image23.png"
img = plt.imread(dado)


plt.subplot(1,2,1)
plt.imshow(img)
plt.axis('off')
plt.title("original")

inv = 1.0 - img
inv[:, :, 3] = img[:, :, 3]

plt.subplot(1,2,2)
plt.imshow(inv)
plt.axis('off')
plt.title("Imagen invertida")
plt.show()