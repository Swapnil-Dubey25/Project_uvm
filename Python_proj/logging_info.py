import logging
import sys

def setup_logging():
    # 1. Create a root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Capture everything at the root level

    # 2. Create a handler for the CLI Console (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # CLI users usually only want INFO and above
    
    # Simple, clean format for the terminal
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # 3. Optional: Create a handler for a background Log File
    file_handler = logging.FileHandler('app.log', mode='a')
    file_handler.setLevel(logging.DEBUG)  # Save detailed debug info to the file
    
    # Detailed format for debugging files (includes timestamps)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

# Initialize logging at the very start of your CLI script
setup_logging()

# --- Your CLI Application Logic ---
def main():
    logging.info("Application started.")
    
    try:
        logging.debug("Attempting to connect to database...") # Only goes to file
        # Simulating a minor issue
        logging.warning("Database connection is slow.")       # Goes to console AND file
        
        # Simulating a crash
        raise ValueError("Invalid configuration detected.")
        
    except Exception as e:
        logging.error(f"A critical error occurred: {e}")      # Goes to console AND file

if __name__ == "__main__":
    main()