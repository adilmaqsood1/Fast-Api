from loguru import logger
import sys
from pathlib import Path

# Define log directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Log file path
LOG_FILE = LOG_DIR / "app.log"

# Remove default loguru handler
logger.remove()

# Configure logging format
logger.add(
    sys.stdout,  
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="DEBUG",
)

logger.add(
    LOG_FILE,  
    rotation="10MB",  # Rotate logs when they reach 10MB
    retention="7 days",  # Keep logs for 7 days
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} | {message}",
    level="DEBUG",
)

def setup_logging():
    logger.info("Logging is configured.")
