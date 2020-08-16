import os
import pandas as pd
from read_data import output_prediction, read_data

if __name__ == '__main__':
    for root, dirs, files in os.walk('data'):
        for name in files:
            file_path = os.path.join(root,name)
            print(file_path)
            if 'sample' in file_path:
                output_prediction(file_path)
            else:
                read_data(file_path)