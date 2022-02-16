FROM alpine:latest

RUN apk update; apk add curl jq skopeo

COPY getClairResults.sh /

ENTRYPOINT ["sh", "/getClairResults.sh"]
