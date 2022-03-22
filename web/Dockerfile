FROM python:3.8
LABEL maintainer="awei"


WORKDIR /web
COPY . /web/

RUN pip install -r requirements.txt

WORKDIR /web/django_practice_01

VOLUME /web
EXPOSE 8000


CMD python3 manage.py runserver 0.0.0.0:8000
