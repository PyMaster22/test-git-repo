from flask import Flask
import uuid
app=Flask(__name__)

@app.route("/uuid.txt")
def uuidtxt():
	return(uuid.uuid4(),200,{"content-type":"text/plain;charset=utf-8"})

@app.route("/rand/<uuid:seed>")
def randtxt(seed):
	return(uuid.uuid5(uuid.UUID(seed),uuid.UUID(seed)))

if(__name__=="__main__"):
	app.run(host="0.0.0.0",port=8080,debug=0)
