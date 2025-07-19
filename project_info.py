"""
Brain Tumor Classification Project Structure

This file provides an overview of the project structure and organization.
"""

PROJECT_STRUCTURE = """
brain-tumor-classification/
├── README.md                          # Project documentation and setup guide
├── LICENSE                            # MIT License file
├── CHANGELOG.md                       # Version history and changes
├── CONTRIBUTING.md                    # Guidelines for contributors
├── .gitignore                        # Git ignore rules
├── requirements.txt                   # Python dependencies
├── config.py                         # Configuration settings
├── setup.py                          # Automated setup script
├── deploy.py                         # Production deployment script
├── test_app.py                       # Unit tests
├── Dockerfile                        # Docker container configuration
├── docker-compose.yml               # Docker Compose setup
├── 
├── app.py                            # Main Flask web application
├── mainTrain.py                      # Model training script
├── mainTest.py                       # Model testing script
├── BrainTumor.ipynb                 # Jupyter notebook for development
├── 
├── .github/                          # GitHub-specific files
│   └── workflows/
│       └── ci.yml                   # GitHub Actions CI/CD pipeline
├── 
├── models/                           # Pre-trained model files
│   ├── BrainTumor10EpochsCategorical.h5
│   ├── BrainTumor16EpochsCategorical.h5
│   └── BrainTumor50EpochsCategorical.h5
├── 
├── templates/                        # HTML templates
│   ├── index.html                   # Main page template
│   └── import.html                  # Base template
├── 
├── static/                           # Static web assets
│   ├── css/                         # Stylesheets
│   │   ├── bootstrap.min.css       # Bootstrap CSS
│   │   ├── test.css                # Custom styles
│   │   └── ...                     # Other CSS files
│   └── js/                          # JavaScript files
│       ├── jquery.min.js           # jQuery library
│       ├── bootstrap.min.js        # Bootstrap JS
│       ├── newjs.js                # Custom JavaScript
│       └── ...                     # Other JS files
├── 
├── dataset/                          # Training dataset (not in repo)
│   ├── no/                          # Non-tumor images
│   │   ├── no0.jpg
│   │   ├── no1.jpg
│   │   └── ...
│   └── yes/                         # Tumor images
│       ├── yes0.jpg
│       ├── yes1.jpg
│       └── ...
├── 
├── uploads/                          # User uploaded images
│   └── (dynamically created)
├── 
└── pred/                            # Prediction test images
    ├── pred0.jpg
    ├── pred1.jpg
    └── ...
"""

# Core components and their purposes
COMPONENTS = {
    "Web Application": {
        "files": ["app.py", "templates/", "static/"],
        "description": "Flask web interface for image upload and tumor prediction"
    },
    "Machine Learning": {
        "files": ["models/", "mainTrain.py", "mainTest.py", "BrainTumor.ipynb"],
        "description": "CNN model training, testing, and pre-trained models"
    },
    "Configuration": {
        "files": ["config.py", "requirements.txt", ".gitignore"],
        "description": "Project configuration and dependency management"
    },
    "Documentation": {
        "files": ["README.md", "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE"],
        "description": "Project documentation and guidelines"
    },
    "DevOps": {
        "files": ["Dockerfile", "docker-compose.yml", ".github/workflows/", "deploy.py"],
        "description": "Deployment, containerization, and CI/CD pipeline"
    },
    "Testing": {
        "files": ["test_app.py", "setup.py"],
        "description": "Unit tests and automated setup scripts"
    }
}

def print_structure():
    """Print the project structure"""
    print("🧠 Brain Tumor Classification - Project Structure")
    print("=" * 60)
    print(PROJECT_STRUCTURE)
    
    print("\n📦 Core Components:")
    print("-" * 30)
    for component, info in COMPONENTS.items():
        print(f"\n{component}:")
        print(f"  Files: {', '.join(info['files'])}")
        print(f"  Purpose: {info['description']}")

if __name__ == "__main__":
    print_structure()
