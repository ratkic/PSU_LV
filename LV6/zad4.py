import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
import numpy as np

# Učitavanje slike
imageNew = mpimg.imread('example_grayscale.png')

# Pretvaranje slike u 2D matricu piksela
height, width = imageNew.shape
X = imageNew.reshape((-1, 1))  # Trebamo matricu oblika (n_sample, n_feature)

# Primjena KMeans algoritma za kvantizaciju boja
n_clusters = [2, 5, 10, 20]  # Možete mijenjati broj klastera
plt.figure(figsize=(15, 10))

for i, n in enumerate(n_clusters):
    k_means = KMeans(n_clusters=n, n_init=1)
    k_means.fit(X) 
    values = k_means.cluster_centers_.squeeze()
    labels = k_means.labels_
    image_compressed = np.choose(labels, values)
    image_compressed.shape = imageNew.shape
    
    # Prikaz komprimirane slike
    plt.subplot(2, 2, i+1)
    plt.imshow(image_compressed, cmap='gray')
    plt.title(f'K = {n}')
    plt.axis('off')

plt.show()

