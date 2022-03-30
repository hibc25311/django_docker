FROM python:3.8
LABEL maintainer="awei"


WORKDIR /web
COPY . /web/


RUN pip3 install -r requirements.txt


WORKDIR /web/django_practice_01

VOLUME /web
EXPOSE 8000


#ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]