# pull official base image
FROM python:3.11.0a6-alpine3.15

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /code/
