import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

paisaje = "paisaje.png"
caminando = "caminando.png"

paisaje_img = plt.imread(paisaje)
caminando_img = plt.imread(caminando)

print(paisaje_img.dtype)
print(caminando_img.dtype)

print(paisaje_img.shape)
print(caminando_img.shape)

alto, ancho = paisaje_img.shape[:2]

caminando_uint8 = (caminando_img * 255).astype(np.uint8)

caminando_resized = Image.fromarray(caminando_uint8).resize((ancho, alto))

caminando_img = np.array(caminando_resized).astype(np.float32) / 255.0

fusion = (paisaje_img[:, :, :3] + caminando_img[:, :, :3]) / 2.0


A = paisaje_img.astype(np.float32)
B = caminando_img.astype(np.float32)

print(paisaje_img.shape)
print(caminando_img.shape)


plt.figure(figsize=(12, 4))

plt.subplot(1,3,1)
plt.imshow(paisaje_img)
plt.axis('off') 
plt.title("paisaje")

plt.subplot(1,3,2)
plt.imshow(caminando_img)
plt.axis('off') 
plt.title("caminando")

plt.subplot(1,3,3)
plt.imshow(fusion)
plt.axis('off') 
plt.title("fusion")


plt.tight_layout()

plt.show()
'''
alto = min(paisaje_img.shape[0], caminando_img.shape[0])
ancho = min(paisaje_img.shape[1], caminando_img.shape[1])

paisaje_img = paisaje_img[:alto, :ancho]
caminando_img = caminando_img[:alto, :ancho]

fusion = ((paisaje_img*2) + (caminando_img-0.5))/2

if fusion.shape[2] == 4:
    fusion[:, :, 3] = 1.0

    
este no  fusion = (A+B)//2
fusion = np.clip(fusion, 0, 255).astype(np.uint8)
'''

