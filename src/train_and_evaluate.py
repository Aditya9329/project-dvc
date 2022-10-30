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
from urllib.parse import urlparse
import mlflow

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

    print("till here everything is fine")
    target         = [config["base"]["target_col"]]
    # print(target)

    train   = pd.read_csv(train_data_path,sep = ";")
    # print(train)
    test    = pd.read_csv(test_data_path,sep=";")
    # print(test)

    train_y = train[target] 
    # print(train_y)

    test_y  = test[target]
    # print(test_y)
    train_x = train.drop(target,axis=1)
    # print(train_x)
    test_x  = test.drop(target,axis = 1)

##################################MLFLOW##################################################
    mlflow_config = config["mlflow_config"]
    remote_server_uri = mlflow_config["remote_server_uri"]
    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(mlflow_config["experiment_name"])
    with mlflow.start_run(run_name = mlflow_config["run_name"]) as mlops_run:

        lr = LogisticRegression(l1_ratio = l1_ratio,
        random_state = random_state)

        lr.fit(train_x,train_y) 

        predicted_qualities = lr.predict(test_x)

        accuracy  = evaluate(test_y,predicted_qualities)

        # mlflow.log_param()
        mlflow.log_param("l1_ratio",l1_ratio)
        mlflow.log_metric("accuracy",accuracy)
        # mlflow.log_metric()
        # mlflow.log_metric()
        tracking_url_type_score  = urlparse(mlflow.get_artifact_uri()).scheme

        if tracking_url_type_score !="file":
            mlflow.sklearn.log_model(lr,"model",registered_model_name=mlflow_config["registered_model_name"])

        else:
            mlflow.sklearn.load_model(lr,"model")

    #############################################################################
        scores_file = config["reports"]["scores"]
        params_file = config["reports"]["params"]
        with open(scores_file,"w")  as f:
            scores = {
                "accuracy" :accuracy
            }
            json.dump(scores,f,indent=4)

        with open(params_file,"w")  as f:
            params = {
                "l1_ratio" :l1_ratio
            }
            json.dump(params,f,indent=4)
        

        print("Accuracy_score = ",accuracy)
        #################################################################

        os.makedirs(model_dir,exist_ok=True)
        model_path = os.path.join(model_dir,"models.joblib")
        joblib.dump(lr,model_path)



        

    if __name__ == "__main__":
        args = argparse.ArgumentParser()
        args.add_argument("--config",default = "params.yaml")
        parsed_args = args.parse_args()
        train_and_evaluate(config_path = parsed_args.config)

    

