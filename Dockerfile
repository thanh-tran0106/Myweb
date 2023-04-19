FROM ubuntu:latest

MAINTAINER Thanh

RUN apt-get update

RUN apt-get install python3-pip -y

RUN pip3 install pipenv

RUN pip install streamlit

COPY . /app

WORKDIR /app

EXPOSE 8501

ENTRYPOINT streamlit hello
