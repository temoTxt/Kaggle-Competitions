import pandas as pd
from explore_sell_price_data import pass_data

def read_data(file):
    print('You are reading data')
    if 'train' in file:
        read_training_data(file)
    elif 'sell_price' in file:
        print('You are reading sales prices')
        price_data = pd.read_csv(file)
        print(price_data.head)
        pass_data(price_data)
    else:
        comp_data = pd.read_csv(file)
        #print(comp_data.head())

def output_prediction(file):
    print('You are submitting data')
    #submission = pd.read_csv(file)
    #print(submission.head())

def read_training_data(file):
    if 'val' in file:
        read_training_val_data(file)
    elif 'eval' in file:
        read_training_eval_data(file)
    else:
        print('You are reading other data')
        #training_df = pd.read_csv(file)
        #print(training_df.head())

def read_training_eval_data(file):
    print('You are reading evaluation training data')
    #training__eval_df = pd.read_csv(file)
    #print(training__eval_df.head())

def read_training_val_data(file):
    print('You are reading validation data')
    #training_val_df = pd.read_csv(file)
    #print(training_val_df.head())