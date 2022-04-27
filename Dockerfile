FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install python3 -y && apt-get install python3-pip -y
RUN apt-get update -y && apt-get upgrade -y
RUN pip3 install --upgrade pip