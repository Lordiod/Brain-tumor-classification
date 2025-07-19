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
        return """
        <div class="result-positive">
            <div class="result-icon">
                <i class="fas fa-check-circle text-success" style="font-size: 2rem;"></i>
            </div>
            <h4 class="text-success mt-3">No Brain Tumor Detected</h4>
            <p class="result-description">
                The AI analysis of your brain scan indicates <strong>no signs of a brain tumor</strong>. 
                The neural patterns and tissue structures appear normal based on our deep learning model's assessment.
            </p>
            <div class="confidence-indicator">
                <small class="text-muted">
                    <i class="fas fa-info-circle"></i> 
                    This result is based on AI analysis of the provided image
                </small>
            </div>
        </div>
        """
    elif classNo == 1:
        return """
        <div class="result-negative">
            <div class="result-icon">
                <i class="fas fa-exclamation-triangle text-warning" style="font-size: 2rem;"></i>
            </div>
            <h4 class="text-warning mt-3">Potential Brain Tumor Detected</h4>
            <p class="result-description">
                The AI analysis has identified <strong>potential abnormal tissue patterns</strong> that may indicate 
                the presence of a brain tumor. This finding requires immediate medical attention and professional evaluation.
            </p>
            <div class="medical-advice">
                <div class="alert alert-info">
                    <i class="fas fa-user-md"></i>
                    <strong>Recommended Action:</strong> Please consult with a qualified neurologist or radiologist 
                    for comprehensive medical imaging and professional diagnosis.
                </div>
            </div>
            <div class="confidence-indicator">
                <small class="text-muted">
                    <i class="fas fa-info-circle"></i> 
                    This result is based on AI analysis and requires medical verification
                </small>
            </div>
        </div>
        """

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
