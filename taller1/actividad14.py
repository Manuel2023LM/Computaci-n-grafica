import numpy as np
import matplotlib.pyplot as plt


img = plt.imread( "colores.png")


MX = np.max(img, axis=2)
MN = np.min(img, axis=2)
gris = (MX + MN) / 2.0

gris = np.clip(gris, 0, 255).astype(np.float32)

plt.subplot(1,2,1)
plt.imshow(img)
plt.axis('off')
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(gris, cmap="gray")
plt.axis('off')
plt.title("gris midgray")
plt.show()