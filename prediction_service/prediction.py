# import yaml
# import os
# import json
# import joblib
# import numpy as np


# params_path = "params.yaml"
# schema_path = os.path.join("prediction_service","schema_in.json")


# class NotInRange(Exception):
#     def __init__(self,msg="values enters are not in range"):
#         self.msg = msg
#         super().__init__(self,msg)


# class NotInCols(Exception):
#     def __init__(self,msg="Not in columns"):
#         self.msg = msg
#         super().__init__(self.msg)






# def read_params(config_path):
#     with open(config_path) as yaml_file:
#         config = yaml.safe_load(yaml_file)
#     return config


# def predict(data):
#     config = read_params(params_path)
#     # print(config)
#     model_dir_path  = config["webapp_model_dir"]
#     print(model_dir_path)
#     model  = joblib.load(model_dir_path)
#     prediction = model.predict(data).tolist()[0]
#     return prediction


# def get_schema(schema_path = schema_path):
#     with open(schema_path) as json_file:
#         schema = json.load(json_file)
#     return schema

# def validate_input(dict_request):
#     def _validate_cols(col):
#         schema = get_schema()
#         actual_cols = schema.keys()
#         if col not in actual_cols:
#             raise NotInCols

#     def _validate_values(col,val):
#         schema  = get_schema()
#         if not (schema[col]["min"] <= float(dict_request[col]) <= schema[col]["max"]):
#             raise NotInRange

#     for col, val in dict_request.items():
#         _validate_cols(col)
#         _validate_values(col,val)

# def form_response(dict_request):
#     if validate_input(dict_request):
#         data = dict_request.values()
#         data = [list(map(float,data))]
#         response = predict(data)
#         return response


    

# def api_response(dict_request):
#     try:
#         if validate_input(dict_request):
#             data = np.array([list(dict.request.values())])
#             response  = predict(data)
#             response  = {"response":response}
#             return response
#     except Exception as e:
#         response = {"the_excepted_range":get_schema(),"response":str(e)}
#         return response
       