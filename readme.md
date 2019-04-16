# Flask Micro Base Service
If you always waste your time creating sekeleton for your micro service projects you can clone this repo and use it the way you want, modify, change, improve, anything that suit your needs. mosts are container base so you don't need to install directly to your machine. eg. postgres or redis.


# What Includes

## Example Resource
Bellow are available example resources you can used when application are running.

### GET /users
example response payload
```json
[{
	"id": "uuid",
	"username": "user",
	"password": "hash_password"
}]
```
### POST /users
example send payload
```json
{
	"username": "user",
	"password": "pass"
}
```



## Docker
* [redis:5-alpine](https://hub.docker.com/_/redis)
* [postgres:11-alpine](https://hub.docker.com/_/postgres)

## Python libs
* [Flask==1.0.2](http://flask.pocoo.org/)
* [celery==4.3.0](http://www.celeryproject.org/)
* [gunicorn==19.9.0](https://gunicorn.org/)
* [gevent==1.4.0](http://www.gevent.org/)
* [peewee==3.9.4](http://docs.peewee-orm.com/en/latest/)
* [redis==3.2.1](https://github.com/andymccurdy/redis-py)
* [psycopg2-binary==2.8.1](https://pypi.org/project/psycopg2-binary/)
* [python-json-logger](https://github.com/madzak/python-json-logger)
* [environs](https://github.com/sloria/environs)
* [marshmallow](https://marshmallow.readthedocs.io/en/3.0/)
* [PyJWT](https://github.com/jpadilla/pyjwt)
* [passlib](https://bitbucket.org/ecollins/passlib/wiki/Home)
* [pytest==4.4.0](https://docs.pytest.org/en/latest/)
* [flake8==3.7.7](http://flake8.pycqa.org/en/latest/)
* [autopep8==1.4.4](https://pypi.org/project/autopep8/)

# Requirements
* Docker>=17.12.0
  
Exactly, you only need that one ready on your machine.


# Setup
Attach **Redis** and **Postgres** container

```sh
$ docker-compose up -d redis postgres
```

After postgres being attaches to container, Create database **todo** (default database) 

```sh
$ docker-compose exec postgres psql -U user -c "CREATE DATABASE todo"
```

Build and running your app and celery container
```sh
$ docker-compose build app
$ docker-compose run --rm app flask init_db
$ docker-compose up -d app celery
```

Go to http://localhost:5000/status to make sure app container running


# Running celery tasks
Make sure your celery container already up and running, there's just little example tasks you can run in flask shell
```sh
$ docker-compose run --rm app flask shell
```

```python
>>> from app.users.tasks import total_users
>>> total_user = total_users.delay()
>>> total_user.get()
0
```

# Running Test
Test are running inside container using pytest, using sqlite db. it doesn't need container for celery and postgres running.
```sh
$ docker-compose run --rm app pytest
```