from flask import Flask, request, redirect
import sys
import sqlite3
import twilio.twiml
#custom libs
sys.path.append('lib')
from db_calls import *
#flask init
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond_sms():
	"""Respond and greet the caller by name."""
	from_number = request.values.get('From', None)
	msg = request.values.get('Body',None)
	message = "Thank you for your service! Preparing report, please stand by..."
	resp = twilio.twiml.Response()
	resp.message(message)
	if 'ISSUE:' in msg:
        	conn = sqlite3.connect('agralert.db')
		curs = conn.cursor()
		curs.execute("INSERT INTO agr (latitude,longitude,title) VALUES (?,?,?)", (28.54,-81.38,msg))
		conn.commit()		
		curs.execute("SELECT * FROM agr WHERE latitude == 28.54 AND longitude == -81.38")
		farmers = curs.fetchall()
		if farmers:
			message = 'There have been similar reports in that area, please contact 555-555-NASA'
			resp.message(message)
	return str(resp)

@app.route("/grabjson")
def return_json():
	json = sql_2_json()
	return json

if __name__ == "__main__":
	app.run(host='0.0.0.0')
