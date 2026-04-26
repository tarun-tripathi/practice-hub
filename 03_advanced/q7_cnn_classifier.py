# Q7: CNN Image Classifier
# Task: Classify handwritten digits using a Convolutional Neural Network
# Dataset: MNIST (built into Keras, no download needed)
# Model: Conv2D -> MaxPool -> Dense
# Install: pip install tensorflow keras matplotlib
# Docs: https://keras.io

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0
y_train = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Build CNN
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.3),
    Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()

print("Training CNN...")
history = model.fit(X_train, y_train, epochs=5, batch_size=64,
                    validation_split=0.1, verbose=1)

loss, acc = model.evaluate(X_test, y_test_cat)
print(f"
Test Accuracy: {acc:.4f}")

# Plot sample predictions
predictions = model.predict(X_test[:10])
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flatten()):
    ax.imshow(X_test[i].reshape(28, 28), cmap="gray")
    ax.set_title(f"Pred: {np.argmax(predictions[i])} | True: {y_test[i]}")
    ax.axis("off")
plt.tight_layout()
plt.savefig("cnn_predictions.png")
print("Predictions saved as cnn_predictions.png")