import os
import sys
import logging

# Define log format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define log directory & file
log_dir = os.path.abspath("logs")  # Ensure proper path handling
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath, mode="a"),  # "a" for append mode
        logging.StreamHandler(sys.stderr)  # Using stderr instead of stdout
    ]
)

# Get logger instance
logger = logging.getLogger("MLOps_Wine_Quality_Prediction_projectLogger")  # Fixed typo
