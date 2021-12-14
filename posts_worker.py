#
# CPSC449-Proj4
# Posts Worker

#### Brian Fang (brian.fang@csu.fullerton.edu)
#### Nathan Tran (ntran402@csu.fullerton.edu)
#### Ashkon Yavarinia (ashkon@csu.fullerton.edu)
#### Edgar Cruz (ed.cruz76@csu.fullerton.edu)

import greenstalk
import json
import smtplib
import requests

def createPost(username, password, tweet_content):
    data = {
        "username" : username,
        "tweet_content" : tweet_content
    }
    url = "http://localhost:80/posts/"
    r = requests.post(url, json=data ,auth=(username, password))

    return r.status_code

with greenstalk.Client(('127.0.0.1', 11300), watch='posts') as client:
    while(True) :
        # Grab job from client reserve
        job = client.reserve()
        data = json.loads(job.body)
        statusCode = createPost(data['username'], data['password'], data['text'])

        #Connect to email server and set the destination address
        destinationAddress = data['username'] + "@gmail.com"
        server = smtplib.SMTP('localhost:5600')
        server.ehlo()
        server.set_debuglevel(1)
        message = "From: Project4Backend@csu.fullerton.edu\nTo: " + destinationAddress

        #If post is created successfully, statusCode=201 will be returned
        if(statusCode == 201):
            #Delete job if it has successfully completed
            client.delete(job)
            #Notify user of the successful post
            message = message + "\n\nYou successfully posted a tweet!"
            server.sendmail("Project4Backend@csu.fullerton.edu", destinationAddress,
                message)
            server.quit()
        else:
            #Release job back into pool if it failed
            client.release(job)
            #Notify use of the failed post
            message = message + "\n\nYou encountered an error when posting a tweet."
            server.sendmail("Project4Backend@csu.fullerton.edu", destinationAddress,
                message)
            server.quit()
