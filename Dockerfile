# syntax=docker/dockerfile:1.0.0-experimental
FROM python:3.6-alpine
RUN apk add --no-cache bash \
    openssh-client \
    git

COPY . /app
WORKDIR /app

RUN python setup.py install

CMD  []
