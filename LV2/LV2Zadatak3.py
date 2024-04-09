import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
#a
img_bright = img + 0.2

#b
img_rotate = np.rot90(img)

#c
img_flipped = np.flipud(img)

#d
img_resoultion = img[::10, ::10]

#e
half_width = img.shape[1] // 2
img_quarter = np.zeros_like(img)
img_quarter[:, half_width:] = img[:, half_width:]

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0, 0].imshow(img)
axes[0, 0].set_title('Originalna slika')

axes[0, 1].imshow(img_bright)
axes[0, 1].set_title('Posvijetljena slika')

axes[0, 2].imshow(img_rotate)
axes[0, 2].set_title('Rotirana slika')

axes[1, 0].imshow(img_flipped)
axes[1, 0].set_title('Zrcaljena slika')

axes[1, 1].imshow(img_resoultion)
axes[1, 1].set_title('Smanjena rezolucija')

axes[1, 2].imshow(img_quarter)
axes[1, 2].set_title('Druga četvrtina slike')

plt.tight_layout()


plt.imshow(img)
plt.show()
