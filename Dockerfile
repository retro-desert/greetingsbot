FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
ENV DockerHome=/var/www/greetingsbot

LABEL maintainer=retro-desert

RUN mkdir -p $DockerHome
WORKDIR $DockerHome

COPY requirements.txt $DockerHome
RUN pip install -r requirements.txt

ADD . $DockerHome

COPY ./docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
RUN chmod +x /usr/bin/docker-entrypoint.sh