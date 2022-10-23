## load train and test files
## train algo
## saved metrics and params


import os
import sys 
import pandas as pd 
import numpy as np
from sklearn.metrics import mean_squared_error , mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet,LogisticRegression
from sklearn.metrics import accuracy_score
from urllib.parse import urlparse
from get_data import read_params 
import argparse 
import joblib
import json 

def evaluate(actual,pred):
    acc = accuracy_score(actual,pred)
    return acc

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path= config["split_data"]["train_path"]
    random_state   = config["base"]["random_state"]
    model_dir      = config["model_dir"]

    # alpha          = config["estimators"]["LogisticRegression"]["params"]
    l1_ratio       = config["estimators"]["LogisticRegression"]["params"]["l1_ratio"]


    target         = [config["base"]["target_col"]]

    train   = pd.read_csv(train_data_path,sep = ";")
    test    = pd.read_csv(test_data_path,sep=";")

    train_y = train[target] 
    test_y  = test[target]
    train_x = train_x.drop(target,axis=1)
    test_x  = test_x.drop(target,axis = 1)


    lr = LogisticRegresseion(l1_ratio = l1_ratio,
    random_state = random_state)

    lr.fit(train_x,train_y) 

    predicted_qualities = lr.predict(test_x)

    accuracy  = evaluate(test_y,predicted_qualities)

    print("Accuracy_score = ",accuracy)

    os.mkdir(model_dir,exists=True)
    model_path = os.path.join(model_dir,"model.joblib")
    joblib.dump(lr,model_path)
    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path = parsed_args.config)

    

