import pyodbc
import time 
import openpyxl
def logger(Request, Response, Weightage, Status, HitTime):
    Response=str(Response).replace("\'","\"")
    Request=str(Request).replace("\'","\"")
    
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                            'Server=10.1.8.41,62717;'
                            'Database=DIGISALES_UAT;'
                            'UID=DIGISALES_UAT;'
                            'PWD=sud@1234;'
                            )
    
    cursor = conn.cursor()
    query1="SELECT count(*) FROM SURAJ_TEST where Request=\'"+str(Request)+"\'"
    cursor.execute(query1)
    for x in cursor:
        res = ''.join(filter(lambda i: i.isdigit(), str(x)))
    if(int(res)==0):
        query2="INSERT INTO SURAJ_TEST (Request,Response,Weightage,Status,HitTime) VALUES (\'"+str(Request)+"\',\'"+str(Response)+"\',"+str(Weightage)+",\'"+str(Status)+"\',\'"+str(HitTime)+"\');"
        cursor.execute(query2)
        cursor.commit()
    else:
        query3="UPDATE SURAJ_TEST SET HitTime = \'"+str(HitTime)+"\' WHERE Request=\'"+Request+"\'"
        cursor.execute(query3)
        cursor.commit()
    cursor.close()