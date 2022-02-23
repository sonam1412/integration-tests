#!/bin/bash

set -e

#SHA
SHA=$1

#repository
repo=$2

#get the results from clair here, sha format needs to be URL decoded hence the string modification
curl -H "Content-type: application/json" -XGET https://quay.io/api/v1/repository/$repo/manifest/${SHA//:/%3A}/security?vulnerabilities=true | jq
