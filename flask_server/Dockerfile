FROM python:3.7.7

ADD . /flask_server
WORKDIR /flask_server

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT ["flask", "run"]