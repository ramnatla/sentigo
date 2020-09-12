import flask
import os
from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from main import run
from sendEmails import send
import pyrebase
import json

app = Flask(__name__)
api = Api(app)

CORS(app)

firebase_config = {
  "apiKey": os.environ.get("FIREBASE_API_KEY"),
  "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
  "databaseURL": os.environ.get("FIREBASE_DATABASE_URL"),
  "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
  "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
  "serviceAccount": os.environ.get("FIREBASE_SERVICE_ACCOUNT"),
  "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID")
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

@app.route('/<string:event>', methods = ['GET'])
def get(event):

	# Example data
	hardcode = {
		"sentiment": 0.3111,
		"imagesAnalyzed": 0,
		"urls": [
		],
		"positivePosts": [
			"@MLHacks A fun domain name is https://t.co/TcsHYutAdX :^) #MHacks #YesIMadeThisAccountJustForTheMLHThing",
			"I think you are going to need more Fruit Snacks #goblue https://t.co/egTVi6EaiY",
			"Getting our #mhacks on! Come see our @NETSCOUT booth at MHacks 12 on campus this weekend and learn all about what o… https://t.co/Nztk84a00s",
			"Hey @Mhacks! You can win this swag bag from @Domaindotcom by tweeting your most creative domain name with the… https://t.co/LX5yavLTiC"
		],
		"negativePosts": [],
		"postsAnalyzed": 15
	}
	return hardcode, 200
	
	info = run(event)
	return info, 200

@app.route('/event_status/<string:event>', methods = ['GET'])
def isEventBad(event):
	info = {}

	if db.child("BadEvents").get().val() is None:
		info['isBad'] = False
		return jsonify(info), 200
	
	bad_events = db.child("BadEvents").get().val().values()
	bad_events = list(bad_events)

	info['isBad'] = False
	if event in bad_events:
		info['isBad'] = True

	return jsonify(info), 200

@app.route('/enroll_user', methods = ['POST'])
def registerUser():
	email = flask.request.get_json()["email"]
	university = flask.request.get_json()["university"]

	db.child(university).push(email)
	return university, 200

@app.route('/send_report_emails', methods = ['POST'])
def sendWarningEmails():
	event = flask.request.get_json()["event"]
	university = flask.request.get_json()["university"]
	db_events = db.child(university).get().val().values()
	db_events = list(db_events)
	db.child("BadEvents").push(event)
	message_to_send = "According to another SentiGo user, the event: " + event + " happening at " + university +", is unsafe to go to. Please be cautious if attending."
	send(message=message_to_send, to_addrs=db_events)
	return university, 200

app.run(debug=True)