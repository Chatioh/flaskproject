import numpy as np
import struct
from sklearn.model_selection import train_test_split

# Define your custom category mapping
CATEGORY_MAP = {
    0: "Do",
    1: "Cat",
    2: "Bag",
    3: "Shirt",
    4: "Pants",
    5: "Shoes",
    6: "Hat",
    7: "Dress",
    8: "Coat",
    9: "Other"  # Adjust as necessary for your dataset
}

def load_mnist_images(file_path):
    with open(file_path, 'rb') as f:
        magic_number, num_images, rows, cols = struct.unpack('>IIII', f.read(16))
        images = np.frombuffer(f.read(), dtype=np.uint8).reshape(num_images, rows, cols, 1)
        return images

def load_mnist_labels(file_path):
    with open(file_path, 'rb') as f:
        magic_number, num_labels = struct.unpack('>II', f.read(8))
        labels = np.frombuffer(f.read(), dtype=np.uint8)
        return labels

def load_data():
    train_images = load_mnist_images('data/train-images-idx3-ubyte')
    train_labels = load_mnist_labels('data/train-labels-idx1-ubyte')
    test_images = load_mnist_images('data/t10k-images-idx3-ubyte')
    test_labels = load_mnist_labels('data/t10k-labels-idx1-ubyte')
    return train_images, train_labels, test_images, test_labels

def preprocess_data():
    train_images, train_labels, test_images, test_labels = load_data()
    
    # Normalize pixel values to [0, 1]
    train_images = train_images.astype('float32') / 255.0
    test_images = test_images.astype('float32') / 255.0

    # Map numeric labels to custom categories
    train_labels = np.array([CATEGORY_MAP[label] for label in train_labels])
    test_labels = np.array([CATEGORY_MAP[label] for label in test_labels])

    # Split training data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(train_images, train_labels, test_size=0.1, random_state=42)

    return X_train, y_train, X_val, y_val, test_images, test_labels