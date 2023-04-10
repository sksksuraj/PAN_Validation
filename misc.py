from datetime import datetime
def miscFunc(Request, Response, Weightage, Status, HitTime):
    query="INSERT INTO SURAJ_TEST (Request,Response,Weightage,Status,HitTime) VALUES (\'"+str(Request)+"\',\'"+str(Response)+"\',"+str(Weightage)+",\'"+str(Status)+"\',\'"+str(HitTime)+"\'"");"
    
    print(query)
Request="{'Code': '1', 'Result': 'NO_Match', 'NSDL_Response': '1^BCMPM4529B^E^MAHAPATRA^LAXMIDHAR^^Shri^26/02/2021^^Y^\n'}"
request=Request.replace("\'","\"")
t = datetime.now()

miscFunc('{"Pan_Number":"BCMPM4529B","Application_Number":"99995001","Application_Name":"Inward","FName":"Rohit","LName":"Kapdi","Login_Name":"rohit.kapdi","RequestType":"2"}',request, 64, 'FAIL', t )