import greenstalk
import smtplib
import re
import json
import requests
import sqlite3
from sqlite_utils.db import Database

pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

with greenstalk.Client(('127.0.0.1', 11300), watch='polls') as client:
    #open connection to db
    db = Database(sqlite3.connect("./var/users.db"))
    posts = db['posts']

    #Connect to email server and set the destination address
    server = smtplib.SMTP('localhost:5600')
    #server.ehlo()
    
    while True:
        server.set_debuglevel(1)
        server.connect('localhost:5600')

        job = client.reserve()
        data = json.loads(job.body)

        #finds email of user posting 
        username = data["username"]
        email = db.query("SELECT email FROM users WHERE username = ?", (username,)) #db['users'].rows_where("username = :username", {"username": username}, select='email')
        email = next(email)['email']
        message = "From: Project4Backend@csu.fullerton.edu\nTo: " + email
    
        #verifies if poll is valid
        poll = re.findall(pattern, data['text'])[0]
        r = requests.get(poll)
        if r.status_code == 201:
            #posts the tweet
            '''posts.insert(data)
            data["id"] = posts.last_pk'''

            #send success email
            message += "\n\nYou successfully posted a poll!"
            server.sendmail("Project4Backend@csu.fullerton.edu", email, message)
            server.quit()

        else:
            #send fail email
            message += "\n\nYou tried to posted invalid poll."
            server.sendmail("Project4Backend@csu.fullerton.edu", email, message)
            server.quit()
        client.delete(job)