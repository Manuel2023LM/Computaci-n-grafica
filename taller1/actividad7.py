import numpy as np
import matplotlib.pyplot as plt

dado = "image23.png"
img = plt.imread(dado)

magenta = np.copy(img)
magenta[:,:,1] = 0

plt.subplot(1,2,1)
plt.imshow(img)
plt.axis('off')
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(magenta)
plt.axis('off')
plt.title("canal magenta")
plt.show()