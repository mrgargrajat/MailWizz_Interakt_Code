# MailWizz_Interakt_Code
This is the code for automation of mailwizz &amp; interakt whatsapp integration

# WORKING
# -------

# To remove a session,
GET request to URL with {sessionname} : 65.2.33.83:8080/REMOVE/{sessionname}
                                 e.g. : 65.2.33.83:8080/REMOVE/18thAugustHashingMasterclass
                                 
# To get all information of all sessions :
65.2.33.83:8080/GETALL

# To get list of sessions without all info :
65.2.33.83:8080/GET

# To add a session to app.py make a POST request as:
65.2.33.83:8080/ADD/{googlesheet_name}/{sessionname}/{mailwizz_listid}

e.g.
65.2.33.83:8080/ADD/Hashing18thAugRegistrations/18thAugustHashingMasterclass/jk988q5rhw27f

with JSON holding all information like:

{
    "creds": {
        "type": "service_account",
        "project_id": "interaktcheck",
        "private_key_id": "cb99911b377cc6505cf8de5266624b116fa9b28a",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCygJAmUMeP9YP/\nZ5DryhKysAHfl5rUuqMRFrIv6hcndJWEnhlIghh+P297CvcW0sWvYjkA373CktaN\nVF9Vo4YdN7CWcdjJYtKDfrT2IDRPTneTpCosSuPdCzVyRzdlIbLyBjC1X6hbdCJl\nVO2JLhMg2xn8RyIVyAmzQVplwLPaj+V6NX6YPq9Zo/aQZ5s//kM01Daz1RPDmYXe\nB29tJyOVWqnEx5U5QKVyqdQ9BWU0kOsBIovEU9UdN7L0TekfghoW5C6qahjNP8Ss\n6TghRT0jR+ojaq5KAMdqeExbOloskvr40H2eNPJDiWFxvZn/OsP2lgIgchQevDFp\n3jjuZOVpAgMBAAECggEAAtTdFIKDsTdS3/O1CIx6IJ6qn5ubH48+BB4g9vdxZRU+\nxEMGwc/wfVuFFEWqVuYX2oObcGBcNVCDeevx9DI7GnkLl84Crep0+OmDC4QbbaZK\nvss5Rl5swBD2s33zisA5WLNQ7/uZDdRT3Fl3yCKJ4qOfGqbyize9saZ9KC/hmntW\n2VYpz29X1Q2GojvyWxGzOjgVoGTbK3sAbuslECujzf6RuDq0EYYf/Q2E+k8LFIdA\nanx/q58W2GBFyJzipQCVjM3N0QCcZsDKgPbimyLPSP7+MdbHdzXrb+17L6sFyP9Y\n7D6yNj6wGp0HBDw8oI4rEJ4fwVb1bPRuyF4pvzm24QKBgQD1ohJHJFfSglvVjDhq\nl9ylFPwrZTau1fxbzsFcWjAQ+Yo7uMc0ezMSjrMf41LGg91Ah1ftfJQ7kJgMKeOq\nux1qlS0rhZzV8t7QtetXEzOn3rTCZm63g2LO9ARbC/wzHhPvWLLrAs/rcxS38DGC\nBPcb7vkA5h9/fANdIsKReEbDmQKBgQC6CS4JPFWHRfdVLah3wh4jXezj+Twk8Vj5\nPT3+ZLEFHSC3j9O7nXrDYQRX7MRQ21hMqBEhi1el/l0AOqTe2nTC3XWaRHFPPX0w\nMVcBVE/8iVq8qOaMDGV10oKGivga8bvzcxAkXKp8jSfHYa1fIlnpoG2SKAbVa9zz\nBr8y+GpSUQKBgQCdyJgZHt1TGe3HxSTQQ/C2Ej7R2VhBAq/ygWNv4XcS0FjdeBpu\nOd1axFOH3kxjvHy5YLc4lFfb00v4NEhMeZmxx1WWqWNPg41hYBpmeq0p3kMaxRXF\nyB4GdnT9zzsX0vBXRRDZKZtJ0UizxxTmQi5BwUYuL6R4Db9Tamq1ax95sQKBgQCA\nfDyWVlw/zDvRUXJsG96S0Jj+rrEyVpn7sadyXnrALGjfPm+ewVn7PLMyQq0npwZq\nEx2ZzFIhq/bxZI9f9wLzXt6NSD3122Lt+PW9Tkzb/sVzTTfFe/5LDLPnVm2atl/3\n+P0qD/ITia3yj2ydKu1sZMeoTQrDNfboxj0hZ96OsQKBgQC5btw2zVH0es3OLzhe\niMhnY3pDAqBBCGud1VcOAVJJGKvjclT/bO3iE+mZSBRRQNqFkLYpvQJ/lagdHDoM\nE8xI0OFUJpKcL581UHdJpp2LNu8DPi8Jxg4fbuaBKuGby2q1Es/1GjfEOnJIXwus\n/pmacd7hSc+7iZl9b6st1zUCIQ==\n-----END PRIVATE KEY-----\n",
        "client_email": "interakttest@interaktcheck.iam.gserviceaccount.com",
        "client_id": "107325440060734006940",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/interakttest%40interaktcheck.iam.gserviceaccount.com"
        }
}

# AND MAKE SURE GOOGLE SHEET IS SHARED TO client_email as provided in creds.
e.g. in example above, share google sheet with : interakttest@interaktcheck.iam.gserviceaccount.com

# To list screens:
screen -r

# To attach to a screen:
screen -d -r pid.pname
e.g.:
screen -d -r 153387.foo

Now, after this we get in that screen.
If we want to leave that screen just now without affecting the running code,
Type : 'A' and then 'D' (holding control button)

Ctrl + C to stop a code in screen.

"exit" to kill the screen we are in.

# To start a new screen:
screen -S new_screen_name
--- run code ---
Ctrl + (A and then D) to leave screen and come out from it.

# To run a python file
python3 file_name.py
