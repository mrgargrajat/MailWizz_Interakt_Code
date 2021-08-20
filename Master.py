from hmac import new
from slave import *
import time
import requests
import json

URLsessions = "http://65.2.33.83:8080/GET"
URL = "http://65.2.33.83:8080/GETALL"

############ MASTER FUNCTION FOR UPDATES MANAGEMENT

def updateall():
    while True:
        try:
            x = requests.get(URL)
            y = requests.get(URLsessions)
            res = requests.get(URL)
            info_of = json.loads((res.content).decode('utf-8'))   #dictionary
            res2 = requests.get(URLsessions)
            sessions = json.loads((res2.content).decode("utf-8"))
            sessions = sessions['content']
        except:
            print('Error Loading data from API! Closing server.')
        # print(sessions)
        for session in sessions:
            try:
                arr = info_of[session]
                myjson, sheetname, listid = arr[0], arr[1], arr[2]
                # FOR TEST PURPOSE ONLY
                # if sheetname != '22AugDesignAirBnb':
                #     continue
                try:
                    load_sheet(myjson, sheetname)
                except:
                    print('error loading Document')
                    continue
                try:
                    rows = get_new_members()
                except:
                    print('problem getting new members')
                    continue
                try:
                    if len(rows) >= 1:
                        print('updating list for session: ', session)
                        sendmails(rows, listid, session)
                except:
                    print('Error sending emails')
                    continue
            except:
                print('error unidentified')
        time.sleep(180)

############ CALLING MASTER FUNCTION

updateall()
