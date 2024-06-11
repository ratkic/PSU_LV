import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

# Učitavanje modela
model = tf.keras.models.load_model('best_model.keras')

# Funkcija za pripremu slike
def prepare_image(img_path, target_size=(64, 64)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalizacija slike
    return img_array

# Putanja do slike
img_path = 'C:\\Users\\gtsrb\\Test\\20\\01559.png'  

# Priprema slike
img = prepare_image(img_path)

# Predikcija
predictions = model.predict(img)
predicted_class = np.argmax(predictions, axis=1)

# Ispis rezultata
print(f"Predicted class: {predicted_class[0]}")

# Opcionalno: Prikaz slike
plt.imshow(image.load_img(img_path))
plt.title(f"Predicted class: {predicted_class[0]}")
plt.show()
