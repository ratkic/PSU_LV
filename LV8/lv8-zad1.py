from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# 1) Strukturiraj konvolucijsku neuronsku mrezu
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 2) Definiraj karakteristike procesa učenja pomoću .compile
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# 3) Definiraj callbacks
log_dir = "logs/fit/"
tensorboard_callback = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

checkpoint_callback = callbacks.ModelCheckpoint(
    filepath='best_model.keras',
    save_best_only=True,
    monitor='val_accuracy',
    mode='max',
    verbose=1
)

# 4) Provedi treniranje mreže pomoću .fit
history = model.fit(x_train_s, y_train_s, 
                    epochs=10, 
                    validation_split=0.1, 
                    callbacks=[tensorboard_callback, checkpoint_callback])

# 5) Učitaj najbolji model
best_model = keras.models.load_model('best_model.keras')

# Izračunajte točnost mreže na skupu podataka za učenje i skupu podataka za testiranje
train_loss, train_accuracy = best_model.evaluate(x_train_s, y_train_s, verbose=0)
test_loss, test_accuracy = best_model.evaluate(x_test_s, y_test_s, verbose=0)

print(f'Točnost na skupu za učenje: {train_accuracy:.4f}')
print(f'Točnost na skupu za testiranje: {test_accuracy:.4f}')

# 6) Prikažite matricu zabune na skupu podataka za testiranje
y_train_pred = np.argmax(best_model.predict(x_train_s), axis=1)
y_test_pred = np.argmax(best_model.predict(x_test_s), axis=1)

train_conf_matrix = confusion_matrix(y_train, y_train_pred)
test_conf_matrix = confusion_matrix(y_test, y_test_pred)

# Funkcija za prikaz matrice zabune
def plot_confusion_matrix(conf_matrix, class_names):
    plt.figure(figsize=(10, 8))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

class_names = [str(i) for i in range(10)]

print("Matrica zabune za skup podataka za učenje:")
plot_confusion_matrix(train_conf_matrix, class_names)

print("Matrica zabune za skup podataka za testiranje:")
plot_confusion_matrix(test_conf_matrix, class_names)

# Komentari
# Matrica zabune pruža detaljan uvid u to koje klase su pogrešno klasificirane, što može pomoći u daljoj analizi i poboljšanju modela.
