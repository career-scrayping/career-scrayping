FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y

COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN mkdir /app
