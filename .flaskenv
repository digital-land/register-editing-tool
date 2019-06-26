FLASK_APP=application.wsgi
FLASK_DEBUG=True
FLASK_ENV=development
FLASK_CONFIG=config.DevelopmentConfig
SECRET_KEY=thisisasecret
SCHEMA_URL=https://raw.githubusercontent.com/digital-land/alpha-data/master/schema
SCHEMA_API_URL=https://api.github.com/repos/digital-land/alpha-data/contents/schema?ref=master
SQLALCHEMY_DATABASE_URI='sqlite:///site.db'