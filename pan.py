import requests
import json
import ast
import flask
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import time
import warnings
import requests
warnings.filterwarnings('ignore')
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/Suraj',methods=['GET','POST'])
def func():
    url = 'http://panuatapi.sudlife.in/api/PanValidation/PANValidate'
    data={
            "Pan_Number":"GOCPK5740B",
            "Application_Number":"99995001",
            "Application_Name":"Inward",
            "FName":"Nihal Santosh",
            "LName":"Kadam",
            "Login_Name":"rohit.kapdi",
            "RequestType":"2"
        }
    
    data_full_name = data["FName"]+" "+data["LName"]
    r = requests.post(url, data=data)
    response=r.json()
    print(response)
    t = response['NSDL_Response']
    if(t==None):
        return 0
    else:
        x = t.split("^")
        NSDL_pan_no = x[2]
        NSDL_name_1 = x[3]
        NSDL_name_2 = x[4]
        NSDL_name_3 = x[5]
        NSDL_FULL_name= NSDL_name_2+" "+ NSDL_name_1+" "+NSDL_name_3
        score = fuzz.token_sort_ratio(NSDL_FULL_name,data_full_name)
        return score


if __name__=='__main__':
    x=func()
    if(x>=75):
        print("Weightage: "+str(x)+"-->PASSED")
    elif(x==0):
        print("Pan Number is not in correct format -->FAILED")
    elif(x>0 and x<75):
        print("Weightage: "+str(x)+"-->FAILED")
