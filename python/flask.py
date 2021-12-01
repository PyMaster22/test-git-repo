from flask import Flask
import uuid,random
app=Flask(__name__)

@app.route("/uuid.txt")
def uuidtxt():
	return(uuid.uuid4(),200,{"content-type":"text/plain;charset=utf-8"})

@app.route("/rand/<uuid:seed>")
def randtxt(seed):
	return(
