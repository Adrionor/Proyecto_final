import logging
import os

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

def main():
    logging.info("Starting the program...")

    # Create an instance of the SavedFile class
    logging.debug("Creating an instance of the SavedFile class...")
    File = SavedFile(r'my_folder_\My_model\My_model_regression')
    logging.debug("Instance of the SavedFile class has been created successfully.")

    # Check if the file has been saved
    logging.debug("Checking if the file has been saved...")
    File.check_save()
    logging.debug("File check completed.")

    logging.info("Program execution completed.")

if __name__ == "__main__":
    main()
