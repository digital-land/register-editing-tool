# register-editing-tool

Requirements

- [Python 3](https://www.python.org/)
- SQLite

Getting started
---------------

Make a virtualenv for the project and install python dependencies

    pip install -r requirements.txt

Generate a database in a flask shell

	flask shell
	from application.extensions import db
	from application.models import DynamicModel
	db.create_all()
Confirm the database has been created by looking for site.db in the application directory

Run flask server

    flask run  
    
    
Environment variables in .flaskenv already set

    FLASK_APP=application.wsgi
	FLASK_DEBUG=True
	FLASK_ENV=development
	FLASK_CONFIG=config.DevelopmentConfig
	SCHEMA_URL=https://raw.githubusercontent.com/digital-land/alpha-data/master/schema
	SCHEMA_API_URL=https://api.github.com/repos/digital-land/alpha-data/contents/schema?ref=master
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'


