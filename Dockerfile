# Dockerfile
from python:alpine
ENV TCPDUMP_VERSION 4.9.2-r0

WORKDIR /usr/src/app
COPY buttons.py ./
RUN mkdir config
RUN apk add --update tcpdump==${TCPDUMP_VERSION} && rm -rf /var/cache/apk/*
RUN pip3 install scapy-python3 && pip3 install pyyaml && pip3 install requests

CMD [ "python", "buttons.py"]
