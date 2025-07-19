#!/usr/bin/env python3
"""
Production deployment script for Brain Tumor Classification
"""

import os
import sys
import subprocess
import argparse

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def deploy_docker():
    """Deploy using Docker"""
    commands = [
        ("docker build -t brain-tumor-classification .", "Building Docker image"),
        ("docker-compose down", "Stopping existing containers"),
        ("docker-compose up -d", "Starting new containers")
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    print("🎉 Docker deployment completed!")
    print("🌐 Application should be available at http://localhost:5000")
    return True

def deploy_local():
    """Deploy locally with gunicorn"""
    commands = [
        ("pip install -r requirements.txt", "Installing dependencies"),
        ("python setup.py", "Running setup script")
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    print("🚀 Starting application with gunicorn...")
    try:
        subprocess.run([
            "gunicorn", 
            "--bind", "0.0.0.0:5000",
            "--workers", "4",
            "--timeout", "120",
            "app:app"
        ], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Application stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start application: {e}")
        return False
    
    return True

def main():
    """Main deployment function"""
    parser = argparse.ArgumentParser(description="Deploy Brain Tumor Classification app")
    parser.add_argument(
        "--method", 
        choices=["docker", "local"], 
        default="local",
        help="Deployment method (default: local)"
    )
    
    args = parser.parse_args()
    
    print("🧠 Brain Tumor Classification - Deployment Script")
    print("=" * 60)
    
    if args.method == "docker":
        if not deploy_docker():
            sys.exit(1)
    else:
        if not deploy_local():
            sys.exit(1)

if __name__ == "__main__":
    main()
