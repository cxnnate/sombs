FROM python:3.10.6-alpine

USER 0

RUN mkdir /opt/apis
RUN sed -i 's/https/http/' /etc/apk/repositories
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /opt/apis

WORKDIR /opt/apis

RUN python3 -m pip install install -r requirements.txt --no-cache-dir

COPY . /opt/apis

CMD [ "python", "server.py" ]
