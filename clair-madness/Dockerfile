FROM alpine:latest

RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python

COPY getClairResults.py parse.py /
