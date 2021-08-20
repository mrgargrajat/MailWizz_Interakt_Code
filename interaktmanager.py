import requests
from requests import sessions
import json

def callinterakt(name, emailid, code, phone_num, event, sheet, row):
    print('name: ', name,'email id passed: ', emailid, 'code: ', code, 'phone_num: ', phone_num, 'event: ', event)
    user_url = "https://api.interakt.ai/v1/public/track/users/"
    event_url = "https://api.interakt.ai/v1/public/track/events/"
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic LWdMMjVHYkNLa0FibEF0UmhXQ2MtY1Faa21lOWVjYXprR3dHc0VlQ0szbzo='
        }
    phone_num = phone_num % 10000000000
    user_body = {
        "phoneNumber": phone_num,
        "countryCode": code,
        "traits": {
            "name": name,
            "email": emailid,
            event : event
        }
    }
    _session = sessions.session()
    response = _session.post(user_url, headers=headers, json=user_body, timeout= 10)
    res = response.content
    # print(res)
    try:
        # print(type(res))
        res = json.loads(res.decode('utf-8'))
        if res['result'] == 'TRUE':
            sheet.update_cell(row+1, 14, "YES")
            sheet.update_cell(row+1, 20, res['message'])
        else:
            sheet.update_cell(row+1, 14, res['result'])
            sheet.update_cell(row+1, 20, res['message'])
        print('interakt ended successfully')
    except:
        print('error in sheet update by Interakt')
    # return res['result'], res['message']



