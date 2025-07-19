import os
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
from tensorflow.keras.models import load_model
from flask import Flask, request, render_template, jsonify, flash
from werkzeug.utils import secure_filename
import logging
from config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

try:
    # Load model from the models directory
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'BrainTumor16EpochsCategorical.h5')
    model = load_model(model_path)
    logger.info('Model loaded successfully from %s', model_path)
    print('Model loaded. Check http://127.0.0.1:5000/')
except Exception as e:
    logger.error('Failed to load model: %s', str(e))
    model = None

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_className(classNo):
    if classNo == 0:
        return "Based on the results of your provided image, I can reassure you that you do not have a brain tumor."
    elif classNo == 1:
        return "I regret to inform you that the provided image indicate the presence of a brain tumor."

def getResult(img):
    try:
        image = cv2.imread(img)
        if image is None:
            logger.error('Failed to read image: %s', img)
            return None
        
        image = Image.fromarray(image, 'RGB')
        image = image.resize((app.config['INPUT_SIZE'], app.config['INPUT_SIZE']))
        image = np.array(image)
        input_img = np.expand_dims(image, axis=0)
        
        # Use predict instead of predict_classes
        prediction = model.predict(input_img)
        
        # Find the index of the maximum value in the prediction array
        result = np.argmax(prediction, axis=1)
        
        logger.info('Prediction completed successfully')
        return result[0]
    except Exception as e:
        logger.error('Error in prediction: %s', str(e))
        return None

@app.route('/', methods=['GET'])
def index():
    if model is None:
        flash('Model not loaded. Please check the model file.', 'error')
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file selected'}), 400
        
        f = request.files['file']
        
        if f.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(f.filename):
            return jsonify({'error': 'Invalid file type. Please upload an image file.'}), 400
        
        try:
            # Specify the directory where you want to save the uploaded files
            upload_directory = os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'])

            # Check if the directory exists, if not, create it
            if not os.path.exists(upload_directory):
                os.makedirs(upload_directory)

            file_path = os.path.join(upload_directory, secure_filename(f.filename))
            f.save(file_path)
            logger.info('File saved: %s', file_path)
            
            value = getResult(file_path)
            if value is None:
                return jsonify({'error': 'Failed to process the image'}), 500
            
            result = get_className(value)
            logger.info('Prediction result: %s', result)
            return result
        except Exception as e:
            logger.error('Error in upload endpoint: %s', str(e))
            return jsonify({'error': 'An error occurred while processing the image'}), 500
    
    return None

if __name__ == '__main__':
    app.run(debug=True)
