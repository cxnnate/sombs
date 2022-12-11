FROM python:3.10.6-alpine

USER 0

RUN mkdir /opt/twitter

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /opt/twitter

WORKDIR /opt/twitter

RUN python3 -m pip install install -r requirements.txt --no-cache-dir

COPY . /opt/twitter

CMD [ "python", "server.py" ]