# Top.it Backend

Django and Django REST Framework For Top.it

##Changelog

#####02/28/16
* Add initial readme instructions
* fix error, add user, profile, challenge initial views/serializers

##Usage

#### Python Virtual Machine (Unix)

1. `source venv/bin/activate` - Load the environment, run scripts and develop under environment
2. `deactivate` - Unload the environment when you're done working


#Installation

#### Python Virtual Environment

This project is best ran in a virtual environment. You can use pyvenv,
which comes with python 3 and greater. The virtual enviroment lets you run
different versions of python and packages from other projects.

First install python3+ on your machine and then download and install [pip][1].
Then from the root of the project run:

1. `pyvenv env` - Create a virtual environment in the venv folder
2. `source env/bin/activate` - Load the environment
3. `pip install -r requirements.txt` - Install dependencies

NOTE:

`deactivate` - Unloads the environment (Once finished working)

#### PostgreSQL

Download the latest version of PostgreSQL, and follow the instructions for installing
on your system. Once it has been installed, you need to start the PostgreSQL server and open a psql command prompt:

```
CREATE DATABASE topitdb;
\connect topitdb
CREATE USER django WITH PASSWORD 'django' CREATEDB;
\q
```

#### Django

After your database is setup, run these django commands:

* `python manage.py createsuperuser` - add yourself to the database as an admin so that you can login to the REST API
* `python manage.py makemigrations` - create django schema
* `python manage.py makemigrations restapi` - create restapi schema
* `python manage.py migrate` - apply model changes
* `python manage.py runserver` - run test server default is http://localhost:8000


## Deletion

If restarting the database from scratch:

psql prompt:

```
DROP DATABASE neatdb;
\q
```

terminal prompt:
```
rm -rf restapi/migrations/
```