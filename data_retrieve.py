import json
import requests

from datetime import date
import wikipedia as wiki

yearlist=[]
eventlist=[]
def retrievefordm(month, day):
    response = requests.get(
        f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{month}/{day}")
    response = json.loads(response.content)

    print("Here's what happened on this day:")
    for event in response["events"]:
        eventlist.append(event["text"])
        yearlist.append(event["year"])
        
    


    


