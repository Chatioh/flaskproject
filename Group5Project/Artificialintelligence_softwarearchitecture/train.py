import numpy as np
import pickle
from data_loader import preprocess_data
from model import create_model

def train_model():
    X_train, y_train, X_val, y_val, test_images, test_labels = preprocess_data()
    model = create_model()
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
    
    # Save the model in HDF5 format
    model.save('models/mnist_cnn.h5')  
    
    # Save the model in .pkl format
    with open('models/mnist_cnn.pkl', 'wb') as pkl_file:
        pickle.dump(model, pkl_file)

    return model, test_images, test_labels

if __name__ == "__main__":
    train_model()