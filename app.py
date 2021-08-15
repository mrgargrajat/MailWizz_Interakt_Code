from flask import Flask, jsonify, request
import json, requests

################## APP INITIALIZATION

app = Flask(__name__)

################## SMART STORAGE DEVICES

sessionsnames = []
sessions = {}

#md122xqsv06c4#### ROUTE FOR LANDING PAGE

@app.route('/')
def landingpage():
    return '<H1>Hi there. Hold on, we are hacking your device...</H1>'

################## ROUTE TO GET EXISTING SESSIONS

@app.route('/GET')
def existing_sessions():
    res = json.dumps({'status': 200, 'content': sessionsnames})
    return res


################## ROUTE TO ADD A SESSION WITH BIG JSON OBJ FOR CREDENTIALS OF SHEET

@app.route('/ADD/<string:sheetname>/<string:sessionname>/<string:listid>', methods = ['POST'])
def new_sessions(sheetname, sessionname, listid):
    if len(sessionsnames) >= 20:
        return jsonify({'status': 200, 'content': 'We already have 20 sessions running. Please remove some session to add new one'})
    if sessionname in sessionsnames:
        return jsonify({'status': 200, 'content': 'Duplicate Session Name'})
    sessionsnames.append(sessionname)
    # creds
    creds = request.get_json('creds')
    creds = creds['creds']
    sessions[sessionname] = [creds, sheetname, listid]
    return jsonify({'status': 200, 'content': 'SUCCESS'})


################## ROUTE TO REMOVE A SESSION

@app.route('/REMOVE/<string:s>')
def delete_session(s):
    if s not in sessionsnames:
        return jsonify({'status': 200, 'content': 'Session Not Found'})
    sessionsnames.remove(s)
    del sessions[s]
    return jsonify({'status': 200, 'content': 'REMOVED SESSION SUCCESSFULLY'})

################## ROUTE FOR GETTING ALL INFO

@app.route('/GETALL')
def giveall():
    res = sessions
    return res


app.run(host='0.0.0.0', port = 8080)
