FROM alpine:latest

RUN apk update; apk add curl jq

COPY getClairResults.sh /

ENTRYPOINT ["sh", "/getClairResults.sh"]
