import numpy as np
import matplotlib.pyplot as plt

dado = "image23.png"
img = plt.imread(dado)

verde = np.copy(img)
verde[:,:,0] = 0
verde[:,:,2] = 0

plt.subplot(1,2,1)
plt.imshow(img)
plt.axis('off')
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(verde)
plt.axis('off')
plt.title("canal verde")
plt.show()