#!/usr/bin/env python
import json
from datetime import datetime
import tzlocal

with open('15sep.json') as jsonFile:
    data = json.load(jsonFile)

summary = dict()
localTimezone = tzlocal.get_localzone()
fileOut = open('referencia15.tsv', 'w')

for key in data['hourly']:
    summary[key['dt']] = [ key['temp'] , key['humidity'] ]
    localTime = datetime.fromtimestamp(key['dt'], localTimezone)
    fileOut.write( localTime.strftime("%Y-%m-%d %H:%M:%S") +"\t"+str(key['temp'])+"\t"+str(key['humidity'])+"\n" )
