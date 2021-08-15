from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request
import gspread, json
app = Flask(__name__)

forms = []
spreadsheetinfo = {}

def updatesheet(leadinfo):
    lead = json.dumps(leadinfo)
    lead = json.loads(lead)
    total_data = sheet.get_all_records()
    newidx = (int)(len(total_data) + 2)
    keys = ['Timestamp', 'Name', 'Email', 'Phone Number', 'College/Company Name', 'College year/years of experience', 'Dream Company', 'Gender']
    # print(lead)
    # print(type(lead))
    sheet.update_cell(newidx, 1, newidx-1)
    for i in range(int(len(keys) + 1)):
        try:
            if i == 0:
                continue
            sheet.update_cell(newidx, i+1, lead[keys[i-1]])
        except:
            pass
    try:
        sheet.update_cell(newidx, len(keys) + 2, "lead from Facebook")
    except:
        pass
    print('successfully updated')

def opensheet(myjson, sheetname):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(myjson, scope)
    # print(creds)
    client = gspread.authorize(creds)
    global sheet
    sheet = client.open(sheetname).sheet1

@app.route('/add', methods = ['POST'])
def getjson():
    print("we're here")
    data = request.get_json('leadinfo')
    print("Got data")
    entry = data['leadinfo']
    creds = 0
    # creds = data['creds']
    if entry['formID'] in forms:
        allinfo = spreadsheetinfo[entry['formID']]
        # print(type(allinfo))
        allinfo = json.loads(allinfo)
        # print(type(allinfo))
        creds = allinfo['creds']
        sheetname = allinfo['sheetName']
        print("Purified data")
        # print(entry)
        # print(creds)
        opensheet(creds, sheetname)
        updatesheet(entry)
        return {'status': 200, 'content': 'SUCCESS'}
    else:
        return {'status': 200, 'content': 'Failed! Form unknown to creds'}

@app.route('/addinmap', methods = ['POST'])
def getconnection():
    # print('we here')
    data = request.get_json('leadinfo')
    # print("Got data")
    formId = data['formID']
    if formId in forms:
        return {'status': "Duplicate form IDs are not allowed. Try again.", 'response': 200}
    forms.append(formId)
    try:
        spreadsheetinfo[formId] = json.dumps(data['spreadsheetInfo'])
        return {'status': 200, 'content': "SUCCESS"}
    except:
        return {'status': 200, 'content': "FAILED"}

@app.route('/getall')
def getall():
    return {'All JSONs': spreadsheetinfo}

@app.route('/delete/<string:formId>')
def deleteform(formId):
    if formId not in forms:
        return {'status': 200, 'content': 'form Not found!'}
    forms.remove(formId)
    del spreadsheetinfo[formId]
    return {'status': 200, 'content': 'Form deleted successfully'}

@app.route('/get/<string:name>')
def get(name):
    return {'name': name}

app.run(host='0.0.0.0', port = 8000)
