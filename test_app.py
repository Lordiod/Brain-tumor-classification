"""
Simple tests for the Brain Tumor Classification application
"""

import os
import sys
import unittest
import tempfile
from unittest.mock import patch, MagicMock

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestBrainTumorApp(unittest.TestCase):
    """Test cases for the Brain Tumor Classification app"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
    
    def test_config_import(self):
        """Test that config can be imported"""
        try:
            from config import Config
            self.assertIsNotNone(Config.INPUT_SIZE)
            self.assertEqual(Config.INPUT_SIZE, 64)
        except ImportError:
            self.fail("Could not import config")
    
    def test_allowed_extensions(self):
        """Test file extension validation"""
        from config import Config
        allowed_extensions = Config.ALLOWED_EXTENSIONS
        
        self.assertIn('jpg', allowed_extensions)
        self.assertIn('jpeg', allowed_extensions)
        self.assertIn('png', allowed_extensions)
    
    def test_directory_structure(self):
        """Test that required directories exist or can be created"""
        required_dirs = ['models', 'templates', 'static']
        
        for directory in required_dirs:
            dir_path = os.path.join(self.test_dir, directory)
            self.assertTrue(os.path.exists(dir_path), f"Directory {directory} should exist")
    
    def test_template_files(self):
        """Test that template files exist"""
        template_files = ['index.html', 'import.html']
        templates_dir = os.path.join(self.test_dir, 'templates')
        
        for template_file in template_files:
            file_path = os.path.join(templates_dir, template_file)
            self.assertTrue(os.path.exists(file_path), f"Template {template_file} should exist")
    
    @patch('app.model')
    def test_get_class_name(self, mock_model):
        """Test the get_className function"""
        try:
            from app import get_className
            
            # Test no tumor case
            result_no_tumor = get_className(0)
            self.assertIn("do not have", result_no_tumor.lower())
            
            # Test tumor case
            result_tumor = get_className(1)
            self.assertIn("presence of", result_tumor.lower())
            
        except ImportError:
            self.fail("Could not import get_className from app")
    
    def test_model_files_exist(self):
        """Test that at least one model file exists"""
        models_dir = os.path.join(self.test_dir, 'models')
        if os.path.exists(models_dir):
            model_files = [f for f in os.listdir(models_dir) if f.endswith('.h5')]
            self.assertGreater(len(model_files), 0, "At least one .h5 model file should exist")

class TestModelTraining(unittest.TestCase):
    """Test cases for model training functionality"""
    
    def test_dataset_directory(self):
        """Test that dataset directory exists"""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        dataset_dir = os.path.join(test_dir, 'dataset')
        
        if os.path.exists(dataset_dir):
            # Check for subdirectories
            self.assertTrue(os.path.exists(os.path.join(dataset_dir, 'no')))
            self.assertTrue(os.path.exists(os.path.join(dataset_dir, 'yes')))
    
    def test_train_script_exists(self):
        """Test that training script exists"""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        train_script = os.path.join(test_dir, 'mainTrain.py')
        self.assertTrue(os.path.exists(train_script))

def run_tests():
    """Run all tests"""
    print("🧠 Running Brain Tumor Classification Tests")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestBrainTumorApp))
    suite.addTests(loader.loadTestsFromTestCase(TestModelTraining))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed.")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
