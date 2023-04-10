import requests
from fuzzywuzzy import fuzz
from flask import Flask, request, jsonify
import connectdb
from datetime import datetime
app = Flask(__name__)
@app.route('/panValidation',methods=['GET','POST'])
def PanValidation():
    URL=r"http://panuatapi.sudlife.in/api/PanValidation/PANValidate"
    data = request.json
    print(data)
    r=requests.post(URL,data=data)
    response=r.json()
    print(response)
    Fullname=response['NSDL_Response'].split("^")[3]+" "+response['NSDL_Response'].split("^")[4]+" "+response['NSDL_Response'].split("^")[5]
    weightage= fuzz.token_sort_ratio(Fullname,data["FName"]+" "+data["LName"])
    if(weightage==0):
        remarks="Invalid PAN -->FAIL"
    elif(weightage>0 and weightage<75):
        remarks="FAIL"
    elif(weightage>75):
        remarks="PASS"
    t = datetime.now()
    connectdb.logger(data,response,weightage,remarks,t)
    return jsonify(Remarks=remarks ,
                   Weightage=weightage
                    )   
if __name__ =='__main__':  
    app.run(debug = True)