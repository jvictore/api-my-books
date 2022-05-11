FROM ubuntu:bionic

RUN apt update -y && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt install python3.9 -y && apt-get install python3-pip -y
RUN apt-get update -y && apt-get upgrade -y
RUN pip3 install --upgrade pip
RUN apt-get update && apt-get upgrade

WORKDIR /app
COPY . /app

RUN apt install libmysqlclient-dev python3-dev --fix-missing -y
RUN pip3 --no-cache-dir install -r requirements.txt

ENV FLASK_APP=app.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]