from flask import Flask, request, render_template
import numpy as np
import pickle
from PIL import Image
from keras.preprocessing import image as keras_image

app = Flask(__name__)

# Load the model from .pkl file
with open('models/mnist_cnn.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# Define your category mapping
CATEGORY_MAP = {
    0: "Bags",
    1: "Cats",
    2: "Dogs",
    3: "Shirts",
    4: "Pants",
    5: "Shoes",
    6: "Hats",
    7: "Coats",
    8: "Books",
    9: "Others"  # Extend according to your model's classes
}

def preprocess_image(img):
    # Resize the image to 28x28
    img = img.resize((28, 28))
    img_array = keras_image.img_to_array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', result=None)  # Render the upload form without result

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400

    try:
        # Open the image file and convert to grayscale
        img = Image.open(file).convert('L')  # Convert to grayscale
        processed_img = preprocess_image(img)  # Preprocess the image
        prediction = model.predict(processed_img)  # Make a prediction
        result_index = int(np.argmax(prediction))  # Get the predicted class
        result_category = CATEGORY_MAP[result_index]  # Map to category name
        
        return render_template('index.html', result=result_category)  # Render with the result
    except Exception as e:
        return f"Error processing image: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)