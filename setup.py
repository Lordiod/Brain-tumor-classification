#!/usr/bin/env python3
"""
Setup script for Brain Tumor Classification project
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing requirements: {e}")
        return False
    return True

def create_directories():
    """Create necessary directories"""
    directories = ['uploads', 'models', 'static/css', 'static/js']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Created directory: {directory}")
        else:
            print(f"✓ Directory already exists: {directory}")

def check_model_files():
    """Check if model files exist"""
    model_files = [
        'models/BrainTumor10EpochsCategorical.h5',
        'models/BrainTumor16EpochsCategorical.h5',
        'models/BrainTumor50EpochsCategorical.h5'
    ]
    
    missing_files = []
    for model_file in model_files:
        if not os.path.exists(model_file):
            missing_files.append(model_file)
        else:
            print(f"✓ Found model: {model_file}")
    
    if missing_files:
        print("\n⚠ Warning: The following model files are missing:")
        for file in missing_files:
            print(f"  - {file}")
        print("You'll need to train the models or download them before running the application.")
    
    return len(missing_files) == 0

def main():
    """Main setup function"""
    print("🧠 Brain Tumor Classification - Setup Script")
    print("=" * 50)
    
    # Create directories
    print("\n1. Creating directories...")
    create_directories()
    
    # Install requirements
    print("\n2. Installing Python packages...")
    if not install_requirements():
        return
    
    # Check model files
    print("\n3. Checking model files...")
    models_exist = check_model_files()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed!")
    
    if models_exist:
        print("\n✓ All model files found. You can now run the application:")
        print("  python app.py")
    else:
        print("\n⚠ Some model files are missing. You can:")
        print("  1. Train new models: python mainTrain.py")
        print("  2. Or download pre-trained models to the 'models/' directory")
        print("  3. Then run the application: python app.py")

if __name__ == "__main__":
    main()
