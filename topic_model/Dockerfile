FROM baseImage 

USER 0

RUN mkdir/opt/twitter

COPY requirements.txt /opt/twitter

WORKDIR /opt/twitter

# RUN apk update
# RUN apk add make auto make gcc g++ subversion python3-dev

RUN python3 -m pip install install -r requirements.txt --no-cache-dir

COPY . /opt/twitter

CMD ["python" "server.py" ]