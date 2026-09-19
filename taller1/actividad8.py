import numpy as np
import matplotlib.pyplot as plt

dado = "image23.png"
img = plt.imread(dado)

cyan = np.copy(img)
cyan[:,:,0] = 0

plt.subplot(1,2,1)
plt.imshow(img)
plt.axis('off')
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(cyan)
plt.axis('off')
plt.title("canal cyan")
plt.show()