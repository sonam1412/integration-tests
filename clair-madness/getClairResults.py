#!/usr/bin/env python

import requests
import sys
import json

# check for arguments probably...
sha = sys.argv[1]
repo = sys.argv[2]

# this needs to be updated whenever clair is back online on quay.io
url = "https://quay.io/api/v1/repository/{}/manifest/{}/security?vulnerabilities=true".format(repo, sha.replace(":","%3A"))
headers = {'content-type': 'application/json'}

def main(): 
   clairResults = requests.get(url,headers=headers)
   #pretty print json
   print(json.dumps(clairResults.json(), indent=4, sort_keys=True))

if __name__ == "__main__":
   main()
