#
# CPSC449-Proj3
# Registry

import hug
import threading
import requests

registry = []

def healthChecker():
    while True:
        r = requests.get(url='asd')#url of service
        if r.status_code != 200:
            pass #remove service from registry

@hug.startup()
def healthCheck():
    x = threading.Thread(target=healthChecker, args=(), daemon=True)
    x.start()

@hug.post("/register/", status=hug.falcon.HTTP_201)
def register(response, name:hug.types.text, url:hug.types.text):
    pass
    #if {name:url} is not in registry
        #add to registry

@hug.get("/health-check/")
def getRegistry(response):
    return registry #