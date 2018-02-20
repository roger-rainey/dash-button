A simple dash button program to intercept ARP calls from dash buttons to call a service in home-assistant.
http://home-assistant.io

This program can be extended by adding a different service-type in the yaml file.

contains dockerfile to build this machine. The docker container will need to have privileged access and use --net=HOST or else it will not see any traffic

Example of how to run it
docker build -t docker-image .
; docker run --privileged --net=host --name=dash-buttons -d -v config/:/usr/src/app/config/ docker-image


Image is also on docker hub rrainey/dash-buttons:latest
