import logging
import unittest
import os
'''
from click.testing import CliRunner

from my_folder_ import my_folder_
from my_folder_ import cli
'''
log_file = os.path.join("my_folder_", "tests", "folder.log")

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

class TestMy_folder_(unittest.TestCase):
    def setUp(self):
        logging.debug("Setting up test fixtures...")
        # Add your setup code here
        
    def tearDown(self):
        logging.debug("Tearing down test fixtures...")
        # Add your teardown code here
        
    def test_000_something(self):
        logging.debug("Running Test: test_000_something")
        # Add your test code here
        
    def test_command_line_interface(self):
        logging.debug("Running Test: test_command_line_interface")
        # Add your test code here

def main():
    logging.info("Starting the tests...")
    
    # Run the test cases
    logging.debug("Running the test cases...")
    unittest.main()
    
    logging.info("Tests completed.")

if __name__ == '__main__':
    main()
