#!/bin/bash

set -e

#NVR spec
PullSpec=$1

#get the digest here
SHA=$(skopeo inspect -f '{{ .Digest }}' docker://quay.io/$PullSpec)

#get the results from clair here
curl -H "Content-type: application/json" -XGET https://quay.io/api/v1/repository/$(echo $PullSpec | cut -f1 -d":")/manifest/${SHA//:/%3A}/security?vulnerabilities=true | jq
