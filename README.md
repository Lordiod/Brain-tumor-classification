# Brain Tumor Classification Using Deep Learning

A web application for brain tumor detection using Convolutional Neural Networks (CNN) and Flask. This project uses deep learning to classify MRI brain scans and determine the presence or absence of brain tumors.

## Features

- **Deep Learning Model**: Uses CNN for accurate brain tumor classification
- **Web Interface**: User-friendly Flask web application
- **Real-time Prediction**: Upload an image and get instant results
- **High Accuracy**: Trained model with multiple epoch configurations
- **Responsive Design**: Clean and modern UI with Bootstrap

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: TensorFlow, Keras
- **Image Processing**: OpenCV, PIL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Data Processing**: NumPy, scikit-learn

## Project Structure

```
├── app.py                          # Main Flask application
├── mainTrain.py                    # Model training script
├── mainTest.py                     # Model testing script
├── BrainTumor.ipynb               # Jupyter notebook for development
├── requirements.txt               # Python dependencies
├── models/                        # Trained model files
│   ├── BrainTumor10EpochsCategorical.h5
│   ├── BrainTumor16EpochsCategorical.h5
│   └── BrainTumor50EpochsCategorical.h5
├── dataset/                       # Training dataset
│   ├── no/                        # Non-tumor images
│   └── yes/                       # Tumor images
├── templates/                     # HTML templates
│   ├── index.html
│   └── import.html
├── static/                        # Static files (CSS, JS)
├── uploads/                       # Uploaded images directory
└── pred/                          # Prediction test images
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/brain-tumor-classification.git
   cd brain-tumor-classification
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset** (if not included)
   - Place brain MRI images in `dataset/no/` for non-tumor images
   - Place brain MRI images in `dataset/yes/` for tumor images

## Usage

### Running the Web Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://127.0.0.1:5000/`

3. **Upload an MRI image** and click "Predict!" to get the classification result

### Training the Model

To train your own model:

```bash
python mainTrain.py
```

This will:
- Load and preprocess the dataset
- Train the CNN model
- Save the trained model as `.h5` file

### Testing the Model

To test the model with sample images:

```bash
python mainTest.py
```

## Model Architecture

The CNN model consists of:
- Multiple Convolutional layers with ReLU activation
- MaxPooling layers for dimensionality reduction
- Dropout layers for regularization
- Dense layers for final classification
- Binary classification output (Tumor/No Tumor)

## Model Performance

The project includes three pre-trained models:
- **10 Epochs**: Quick training model
- **16 Epochs**: Balanced accuracy and training time
- **50 Epochs**: High accuracy model (recommended)

## API Endpoints

- `GET /` - Home page with upload interface
- `POST /predict` - Upload image and get prediction result

## Dataset

The model is trained on brain MRI images categorized into:
- **No Tumor**: Normal brain MRI scans
- **Tumor**: Brain MRI scans with tumor presence

Dataset source: [Brain Tumor MRI Dataset on Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- TensorFlow and Keras communities for excellent documentation
- Flask framework for web application development
- Bootstrap for responsive UI components

## Disclaimer

⚠️ **Important**: This application is for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis. Always consult with qualified healthcare professionals for medical advice.

## Future Improvements

- [ ] Add more detailed analysis and confidence scores
- [ ] Implement user authentication
- [ ] Add batch processing capability
- [ ] Include more detailed medical information
- [ ] Deploy to cloud platforms (AWS, Heroku, etc.)
- [ ] Add model performance metrics visualization
