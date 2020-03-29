import pandas as pd
from sklearn.linear_model import LogisticRegression
import os
import sys
from joblib import dump, load

class ModelBuilder():

    def __init__(self, data_source: str):
        self.data_source = data_source
        self.curr_dir = os.getcwd() 
        self.make_output_dir()
    
    def run(self):
        train_data, test_data = self.load_data(self.data_source)
        model = self.train(train_data)
        self.save_model(model)
    
    def make_output_dir(self):
        if not os.path.exists(self.curr_dir + "/model"):
            os.makedirs(self.curr_dir + "/model")

    def load_data(self, data_source: str):
        train_data = pd.read_csv(data_source + "/train.csv")
        test_data = pd.read_csv(data_source + "/test.csv")
        return train_data, test_data

    def train(self, train_data: pd.DataFrame):
        X = train_data[['feature']]
        Y = train_data[['label']].values.ravel()
        clf = LogisticRegression(random_state=0).fit(X, Y)
        return clf
    
    def save_model(self, model):
        output_path = os.path.join(self.curr_dir, 'model/model.joblib')
        dump(model, output_path)

# Get the relative directory for the input data
input_data_dir = sys.argv[1]

# Kick of training.
builder = ModelBuilder(input_data_dir)
builder.run()