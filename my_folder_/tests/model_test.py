import logging
import os
import pytest

log_file = os.path.join("my_folder_", "tests", "model.log")

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

class SavedFile:
    def __init__(self, filename):
        self.filename = filename
    
    def check_save(self):
        if os.path.exists(self.filename):
            logging.info("The file has been saved successfully.")
        else:
            logging.warning("The file may not have been saved.")

@pytest.fixture
def saved_file():
    filename = r'my_folder_\My_model\My_model_regression'
    return SavedFile(filename)

def test_check_save(saved_file):
    saved_file.check_save()

if __name__ == "__main__":
    logging.info("Starting the program...")
    # Run the tests
    logging.debug("Running the tests...")
    pytest.main(['-s', '-v'])
    logging.info("Program execution completed.")
