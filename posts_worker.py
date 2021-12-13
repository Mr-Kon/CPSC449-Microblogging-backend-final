#
# CPSC449-Proj4
# Posts Worker

#### Brian Fang (brian.fang@csu.fullerton.edu)
#### Nathan Tran (ntran402@csu.fullerton.edu)
#### Ashkon Yavarinia (ashkon@csu.fullerton.edu)
#### Edgar Cruz (ed.cruz76@csu.fullerton.edu)

import greenstalk
import json
import requests

def createPost(username, password, tweet_content):
    data = {
        "username" : username,
        "tweet_content" : tweet_content
    }
    url = "http://localhost:80/posts/"
    r = requests.post(url, json=data ,auth=(username, password))

    return r.status_code

with greenstalk.Client(('127.0.0.1', 11300)) as client:
    while(True) :
        # Grab job from client reserve
        job = client.reserve()
        data = json.loads(job.body)
        statusCode = createPost(data['username'], data['password'], data['tweet_content'])

        #If post is created successfully, statusCode=201 will be returned
        if(statusCode == 201):
            #Delete job if it has successfully completed
            client.delete(job)
        else:
            #Release job back into pool if it failed
            client.release(job)
