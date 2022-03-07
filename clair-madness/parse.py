#!/usr/bin/env python
import json
import sys

file = open(sys.argv[1])

data = json.load(file)
toIterate = data['data']['Layer']
severity = {'Critical': 0, 'High': 0, 'Medium': 0, 'Low':0, 'Unknown':0}

for each in toIterate['Features']:
   if(each['Vulnerabilities']!=[]):
     for seach in each['Vulnerabilities']:
        if(seach['Severity']=='Critical'):
           severity['Critical'] += 1
        elif(seach['Severity']=='High'):
           severity['High'] += 1
        elif(seach['Severity']=='Medium'):
           severity['Medium'] += 1
        elif(seach['Severity']=='Low'):
           severity['Low'] += 1
        elif(seach['Severity']=='Unknown'):
           severity['Unknown'] += 1

print(severity)
