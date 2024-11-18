import tensorflow as tf
import numpy as np

# Reload model using custom input layer configuration if needed
try:
    model = tf.keras.models.load_model('mnist_cnn_model.h5')
    print("Model loaded successfully.")
except TypeError as e:
    print(f"Error loading model: {e}")
    # Rebuild the model manually to handle deserialization issues
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.load_weights('mnist_cnn_model.h5')

# Load and preprocess MNIST dataset
(_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0
y_test = tf.keras.utils.to_categorical(y_test, 10)

# FGSM attack implementation
def fgsm_attack(model, images, labels, epsilon):
    images_tensor = tf.convert_to_tensor(images)
    labels_tensor = tf.convert_to_tensor(labels)

    with tf.GradientTape() as tape:
        tape.watch(images_tensor)
        predictions = model(images_tensor)
        loss = tf.keras.losses.categorical_crossentropy(labels_tensor, predictions)

    # Compute gradients
    gradient = tape.gradient(loss, images_tensor)
    signed_grad = tf.sign(gradient)

    # Create adversarial examples
    adversarial_examples = images + epsilon * signed_grad
    adversarial_examples = tf.clip_by_value(adversarial_examples, 0, 1)

    return adversarial_examples.numpy()

# Generate adversarial examples
epsilon = 0.1
adv_samples = fgsm_attack(model, x_test[:100], y_test[:100], epsilon)

# Save adversarial samples and labels
np.savez('adversarial_samples.npz', adv_samples=adv_samples, original_labels=y_test[:100])
print("Adversarial samples saved as adversarial_samples.npz")

