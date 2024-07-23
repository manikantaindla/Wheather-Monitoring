# src/test_imports.py
import sys
import os

# Add parent directory of `src` to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import weather_api
    import data_processing
    print("Imports are successful!")
except ImportError as e:
    print(f"Import failed: {e}")
