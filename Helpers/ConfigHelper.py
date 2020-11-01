"""
--- ConfigHelper.py ---
Description: Helps handle config files.
Author - Khoji Ybarra Jr.
Create Date - 09/26/2020
"""
import json
class ConfigHelper:
    # Initializer class to instantiate class level variables
    def __init__(self):
        with open('/home/devox/Documents/plotlyStuff/Config/config.json') as config:
            self.config = json.load(config)
    # Reads and returns files to run in config.json
    def readFilesToRunConfig(self):
        files_to_run = []
        for file in self.config['files_to_run']:
            files_to_run.append((file['file_path']))
        return files_to_run