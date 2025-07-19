import cv2
import os
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load model from models directory
model_path = os.path.join(os.path.dirname(__file__), 'models', 'BrainTumor10EpochsCategorical.h5')
model = load_model(model_path)

# Load test image from pred directory
image_path = os.path.join(os.path.dirname(__file__), 'pred', 'pred2.jpg')
image = cv2.imread(image_path)

img = Image.fromarray(image)
img = img.resize((64, 64))
img = np.array(img)

input_img = np.expand_dims(img, axis=0)

result = np.argmax(model.predict(input_img), axis=1)
print(result)
