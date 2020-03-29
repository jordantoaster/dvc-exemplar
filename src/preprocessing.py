import pandas as pd
from sklearn.model_selection import train_test_split
import os
import sys

class Preprocessing():

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.curr_dir = os.getcwd() 
        self.make_output_dir()
    
    def run(self):
        self.df = self.etl(self.df)
        df_train, df_test = self.split_data(self.df)
        self.save_file(df_train, "train")
        self.save_file(df_test, "test")
    
    def make_output_dir(self):
        if not os.path.exists(self.curr_dir + "/data"):
            os.makedirs(self.curr_dir + "/data")

    def etl(self, df: pd.DataFrame):
        """
        Rudimentary processing, simulates ETL
        """
        df['divided_by_ten'] = df['feature'] / 10
        return df

    def split_data(self, df: pd.DataFrame):
        train, test = train_test_split(df, test_size=0.2)
        return train, test

    def save_file(self, df: pd.DataFrame, data_type: str):
        output_path = os.path.join(self.curr_dir, 'data/' + data_type + '.csv')
        df.to_csv(output_path)

# Get the relative directory for the input data file
input_data_dir = sys.argv[1]
df = pd.read_csv(input_data_dir)

# Process the data for the next stage.
preprocessing = Preprocessing(df)
preprocessing.run()