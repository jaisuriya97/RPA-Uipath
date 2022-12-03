from openpyxl import load_workbook
import pymongo
import os
import gridfs
# **************    Read Excel  ***********
book  = load_workbook('Output.xlsx')
sheet = book.active
rows =sheet.rows
header = [cell.value for cell in next(rows)]
all_rows=[]
for row in rows:
    data = {}
    for title,cell in zip(header,row):
        data[title]=cell.value
    all_rows.append(data)
# *********** db connection *********
try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017
    )
    db = mongo.RPA
    mongo.server_info()
except:
    print("************ Error Cant connnect *************** ")
# ************ Update *************
data = list(db.StudentDetails.find()) 
for Data in data:
    dbname =Data['Name']
    for a in all_rows:
        sample = a['Name']
        if dbname.lower() in sample.lower() :
            if  Data['AadharNumber'] == a['AadharNumber']:
                        user={"Name":f"{dbname}",
                        "Roll":f"{Data['Roll']}",
                        "AadharNumber":a['AadharNumber'],
                        "Address":a['Details'],
                        "Section":Data['Section'],
                        "dep":Data['dep'],
                        "CGPA":Data['CGPA'],
                        "dob":a['DOB']
                }
                        dbresponse = db.MainBase.insert_one(user)