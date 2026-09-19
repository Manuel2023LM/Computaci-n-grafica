import numpy as np
import matplotlib.pyplot as plt


ruta_png = "image.png"
ruta_jpg = "image.jpg"
img = plt.imread(ruta_jpg)

capaR = np.copy(img)


img_png = plt.imread(ruta_png)
img_jpg = plt.imread(ruta_jpg)




ruta = "image.png"

img = plt.imread(ruta)

plt.imshow(img)
plt.axis('off')
plt.show()
