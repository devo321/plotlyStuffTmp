"""
--- CSVHelper.py ---
Description: Helps handle csv files.
Author - Khoji Ybarra Jr.
Create Date - 09/26/2020
"""
import pandas as pd
class CSVHelper:
    # Initializer class to instantiate class level variables
    def __init__(self):
        pass
    # Reads and returns csv into dataframe from given file_name
    @staticmethod
    def read_csv(file_name):
        return pd.read_csv(file_name)
    # Checks if value is float
    @staticmethod
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    # Reads and returns header column
    @staticmethod
    def read_header(data):
        # Checks if first object is float
        if not CSVHelper.isfloat(data[0][0]):
            # Saves header into class variable
            header = data[0]
        else:
            header = []
        return header
    # Merge two arrays based on column_header
    @staticmethod
    def merge_arrays(array1, array2, column_header):
        array1_header_id = CSVHelper.read_header(array1).index(column_header)
        array2_header_id = CSVHelper.read_header(array2).index(column_header)