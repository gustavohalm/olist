FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /olistapp
WORKDIR /olistapp

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /olistapp/

RUN pip install -r /olistapp/requirements.txt

ADD . /olistapp/

# Django service
EXPOSE 8000