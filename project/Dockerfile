# pull official base image
FROM python:3.10.8-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update 
RUN apt-get -y install netcat gcc 
RUN apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --dev --system

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
