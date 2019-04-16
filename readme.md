# Flask Micro Base Service
If you always need more time creating sekeleton for your micro service you can clone this repo and use it the way you want, modify, change, improve, anything that suit your needs. mosts are container base so you don't need to install directly to your machine. eg. postgres or redis.


# What Includes

## Example Resource
* users [POST, GET, DELETE]
* todo [POST, GET, DELETE]

## Docker
* [redis:5-alpine](https://hub.docker.com/_/redis)
* [postgres:11-alpine](https://hub.docker.com/_/postgres)

## Python libs
* [Flask==1.0.2](http://flask.pocoo.org/)
* [celery==4.3.0](http://www.celeryproject.org/)
* [gunicorn==19.9.0](https://gunicorn.org/)
* [meinheld==0.6.1](https://pypi.org/project/meinheld/)
* [peewee==3.9.4](http://docs.peewee-orm.com/en/latest/)
* [redis==3.2.1](https://github.com/andymccurdy/redis-py)
* [psycopg2-binary==2.8.1](https://pypi.org/project/psycopg2-binary/)
* [python-json-logger](https://github.com/madzak/python-json-logger)
* [environs](https://github.com/sloria/environs)
* [marshmallow](https://marshmallow.readthedocs.io/en/3.0/)
* [PyJWT](https://github.com/jpadilla/pyjwt)
* [passlib](https://bitbucket.org/ecollins/passlib/wiki/Home)

# Requirements
* Docker>=17.12.0
  
Exactly, you only need that one ready on your machine.


# Setup
Attach **Redis** and **Postgres** container

```sh
$ docker-compose up -d redis postgres
```

After postgres being attaches to container, Create database todo and todotest
* todo are default db

```sh
$ docker-compose exec postgres psql -U user -c "CREATE DATABASE todo"
$ docker-compose up -d app
```

# Running Test
Test are running inside container using pytest, using sqlite db.
```sh
$ docker-compose run --rm app pytest
```