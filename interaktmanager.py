import requests
from requests import sessions

def callinterakt(name, emailid, code, phone_num, event):
    print('name: ', name,'email id passed: ', emailid, 'code: ', code, 'phone_num: ', phone_num, 'event: ', event)
    user_url = "https://api.interakt.ai/v1/public/track/users/"
    event_url = "https://api.interakt.ai/v1/public/track/events/"
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic LWdMMjVHYkNLa0FibEF0UmhXQ2MtY1Faa21lOWVjYXprR3dHc0VlQ0szbzo='
        }
    eventname = event
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
    print('interakt ended successfully')



