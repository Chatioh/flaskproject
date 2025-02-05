import numpy as np
from keras.models import load_model
from data_loader import load_data

def evaluate_model():
    # Load the test data
    _, _, test_images, test_labels = load_data()

    # Load the model from HDF5 format
    model = load_model('models/mnist_cnn.h5')
    
    # Optionally, load the model from .pkl format
    with open('models/mnist_cnn.pkl', 'rb') as pkl_file:
        model_from_pkl = pickle.load(pkl_file)

    # Evaluate the model
    loss, accuracy = model.evaluate(test_images, test_labels)
    print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

if __name__ == "__main__":
    evaluate_model()