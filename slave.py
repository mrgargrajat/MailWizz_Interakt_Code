import gspread
from oauth2client.service_account import ServiceAccountCredentials
from mailwizz.base import Base
from mailwizz.config import Config
from mailwizz.endpoint.list_subscribers import ListSubscribers
import json
import interaktmanager

sheet = None

################### FUNCTION TO LOAD SHEET FOR PROCESSING

def load_sheet(myjson, sheetname):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(myjson, scope)
    # print(creds)
    client = gspread.authorize(creds)
    global sheet
    sheet = client.open(sheetname).sheet1

################### FUNCTION FOR MAILWIZZ INITIALIZATIONS

def setup():
    try:
        config = Config({
            'api_url': 'http://3.108.194.171/api/index.php',
            'public_key': 'f6a17d25865ed0d927cdd38eaf1681697ee1874e',
            'private_key': 'f6a17d25865ed0d927cdd38eaf1681697ee1874e',
            'charset': 'utf-8'
        })
        Base.set_config(config)
    except:
        print('error in setup')

################### FUNCTION TO GET LIST OF EMAIL RECIEPENTS

def get_new_members():
    result = []
    total_data = sheet.get_all_records()
    row = 1
    for entry in total_data:
        if not entry['MAILWIZZ_SENT']:
            result.append(row)
        row = row+1
    return result

################### FUNCTION TO SEND LIST OF EMAIL RECIEPENTS TO MAILWIZZ

def sendmails(rows, listid, sessionname):
    total = sheet.get_all_records()
    try:
        setup()
        endpointsub = ListSubscribers()
    except:
        print('Mailwizz not working')
    for row in rows:
        entry = total[row-1]
        try:
            response = endpointsub.create(list_uid=listid, data={
                'EMAIL': entry['Email'],
                'FNAME': entry['Full Name'].split(' ')[0],
                'LNAME': entry['Full Name'].split(' ')[1]
            })
            sheet.update_cell(row+1, 13, 'YES')
        except Exception as e:
            print('error at row ',row, ': ', e)
            sheet.update_cell(row+1, 13, str(e))
        if 'YES' in entry['WHATSAPP_SENT'] or 'YES,' in entry['WHATSAPP_SENT']:
            try:
                interaktmanager.callinterakt(entry['Full Name'], entry['Email'], '+91', entry['Phone Number'], sessionname)
                sheet.update_cell(row+1, 14, "YES")
            except Exception as e:
                print("error from interakt: ", e)
                sheet.update_cell(row+1, 14, e)
        else:
            sheet.update_cell(row+1, 14, "NO")

# FOR TEST PURPOSE
# if __name__ == "__main__":
