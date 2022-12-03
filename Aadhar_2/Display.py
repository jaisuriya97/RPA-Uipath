from flask import Flask,render_template,request,flash
import pymongo
app=Flask(__name__)
app.secret_key="iuwbdcishdb"
mongo = pymongo.MongoClient(
        host="localhost",
        port=27017
    )
db = mongo.RPA
mongo.server_info()
@app.route('/',methods=["POST","GET"])
def Display():
    if request.method=="POST":
        name = request.form['name']
        Aadhar=request.form['AadharNumber']
        roll=request.form['roll']
        data=db.MainBase.find()
        for Data in data:
            Dbname=Data['Name']
            DbAadhar=Data['AadharNumber']
            Dbroll=Data['Roll']
            if Dbname.lower() == name.lower() and DbAadhar== Aadhar and Dbroll == roll:
                pData = (Data['Name'],Data['Roll'],Data['dob'],Data['Section'],Data['dep'],Data['AadharNumber'],Data['CGPA'],Data['Address'])

                return render_template("Home.html",Pdata = pData)   
                

    return render_template("Home.html")
if __name__=="__main__":
    app.run(debug=True)