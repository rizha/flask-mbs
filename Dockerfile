FROM python:3.7-alpine

ENV PYTHONBUFFERED 1
ENV C_FORCE_ROOT true
STOPSIGNAL SIGTERM

RUN apk add --virtual build-deps gcc \
    python3-dev musl-dev postgresql-dev

WORKDIR /root

ADD ./requirements.txt .

RUN pip install -r requirements.txt

CMD gunicorn -w 1 -k gevent app -b :5000