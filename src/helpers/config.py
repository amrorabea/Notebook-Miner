import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the directory containing Jupyter notebooks
NOTEBOOK_DIR = os.getenv("download_path")
SAVE_DIR = os.getenv("save_path")
