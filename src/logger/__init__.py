import logging
import os
from datetime import datetime

# Generate the log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where logs will be stored
log_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Create the full path for the log file
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    filename=LOG_FILE_PATH,  # Log file path
    format="[%(asctime)s] - %(name)s - %(lineno)d - %(levelname)s - %(message)s"  # Corrected format as a string
)