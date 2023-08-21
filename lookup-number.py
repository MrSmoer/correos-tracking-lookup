import requests, json, sys, os
from datetime import datetime

DEFAULTFILE="tracking-numbers.txt"
API_ENDPOINT="https://api1.correos.es/digital-services/searchengines/api/v1"

def getStateOfParcel(trackingNumber):
    r = requests.get(API_ENDPOINT, params={"searchType":"envio","language":"EN", "text":trackingNumber})
    #print(r.url)
    #print(r.content)
    return json.loads(r.content.decode("utf-8"))

def getTimeOfEvent(event):
    s = " ".join([event["eventDate"],event["eventTime"]])
    #print(s)
    timestamp = datetime.strptime(s, "%d/%m/%Y %H:%M:%S")
    return timestamp

def main():
    args=sys.argv
    args.pop(0)

    if len(args) == 1 and os.path.exists(args[0]):
        with open(args[0]) as f:
            trackingNumbers = f.readlines()
            #print(trackingNumbers)
    elif len(args) < 1:
        if not os.path.exists(DEFAULTFILE):
            print("no tracking number specified")
            return
        else:
            with open(DEFAULTFILE) as f:
                trackingNumbers = f.readlines()
    else:
        trackingNumbers = args

    trackingNumbers=[s.replace('\n', '') for s in trackingNumbers]


    print("Looking up tracking Numbers: "+str(trackingNumbers))
    states={}
    for trackingNumber in trackingNumbers:
        states[trackingNumber]=trackingNumber,getStateOfParcel(trackingNumber)

    #print(states)

    for delivery in states:

        events=states[delivery][1]['shipment'][0]['events']
        latestEvent=(events[0])
        for event in events:
            if getTimeOfEvent(event) > getTimeOfEvent(latestEvent):
                latestEvent=event

        print("\n"+delivery)
        print(latestEvent)
        print("\n")

if __name__=='__main__':
    main()