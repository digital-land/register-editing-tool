export FLASK_APP=application.app
export SECRET_KEY=heythisissecret!
export SCHEMA_URL=https://raw.githubusercontent.com/digital-land/alpha-data/master/schema
export SCHEMA_API_URL=https://api.github.com/repos/digital-land/alpha-data/contents/schema?ref=master
export FLASK_ENV=development

flask run
