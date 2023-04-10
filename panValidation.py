import requests
from fuzzywuzzy import fuzz
from flask import Flask, request, jsonify
from datetime import datetime
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def PanValidation():
    dummy={
            "Pan_Number": "",
            "Application_Number": "00000000",
            "Application_Name": "x",
            "FName": "",
            "LName": "",
            "Login_Name": "x",
            "RequestType": "2"
          }
    URL=r"http://panuatapi.sudlife.in/api/PanValidation/PANValidate"
    data = request.json
    # print(data)
    dummy["Pan_Number"]=data["Pan_Number"]
    dummy["FName"]=data["FName"]
    dummy["LName"]=data["LName"]
    r=requests.post(URL,data=dummy)
    response=r.json()
    # print(response)
    Fullname=response['NSDL_Response'].split("^")[3]+" "+response['NSDL_Response'].split("^")[4]+" "+response['NSDL_Response'].split("^")[5]
    weightage= fuzz.token_sort_ratio(Fullname,data["FName"]+" "+data["LName"])
    if(weightage==0):
        remarks="Invalid PAN -->FAIL"
    elif(weightage>0 and weightage<75):
        remarks="FAIL"
    elif(weightage>75):
        remarks="PASS"
    t = datetime.now()
    # connectdb.logger(data,response,weightage,remarks,t)
    return jsonify(Remarks=remarks ,
                   Weightage=weightage
                    )

@app.errorhandler(404)
def handle_bad_request(e):
    return jsonify({'error':'Not found'})

@app.errorhandler(500)


def handle_bad_request(e):
    return jsonify({'error':'Internal server error'})
 
if __name__ =='__main__':  
    app.run(debug = True)