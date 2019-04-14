FROM python:3.7-alpine

ENV PYTHONBUFFERED 1
ENV C_FORCE_ROOT true
STOPSIGNAL SIGTERM

RUN apk add --virtual build-deps gcc \
    python3-dev musl-dev postgresql-dev

WORKDIR /root

ADD ./requirements.txt .

RUN pip install -r requirements.txt

RUN apk del build-deps

CMD gunicorn -w 2 -k meinheld.gmeinheld.MeinheldWorker wsgi:app -b :5000