import os
import pandas as pd

def read_data(file):
    print('You are reading data')
    if 'train' in file:
        read_training_data(file)
    else:
        comp_data = pd.read_csv(file)
        print(comp_data.head())

def output_prediction(file):
    print('You are submitting data')
    submission = pd.read_csv(file)
    print(submission.head())

def read_training_data(file):
    if 'val' in file:
        read_training_val_data(file)
    elif 'eval' in file:
        read_training_eval_data(file)
    else:
        print('You are reading training data')
        training_df = pd.read_csv(file)
        print(training_df.head())

def read_training_eval_data(file):
    print('You are reading evaluation training data')
    training__eval_df = pd.read_csv(file)
    print(training__eval_df.head())

def read_training_val_data(file):
    print('You are reading validation data')
    training_val_df = pd.read_csv(file)
    print(training_val_df.head())


if __name__ == '__main__':
    for root, dirs, files in os.walk('data'):
        for name in files:
            file_path = os.path.join(root,name)
            print(file_path)
            if 'sample' in file_path:
                output_prediction(file_path)
            else:
                read_data(file_path)