import numpy as np
import matplotlib.pyplot as plt


G = plt.imread( "colores.png")

T = G.astype(np.float32)

img = 0.299*T[:,:,0] + 0.587*T[:,:,1] + 0.114*T[:,:,2]
img = np.clip(img, 0, 255).astype(np.float32)

plt.subplot(1,2,1)
plt.imshow(G)
plt.axis('off')
plt.title("original")

plt.subplot(1,2,2)
#plt.figure("escala del gris luminosity")
plt.imshow(img, cmap="gray")
plt.axis('off')
plt.title("gris luminosity")
plt.show()