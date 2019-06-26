from flask import Flask


def create_app(config_filename):
   app = Flask(__name__)
   app.config.from_object(config_filename)
   register_blueprints(app)
   register_extensions(app)

   # register_errorhandlers(app)
   # register_extensions(app)
   # register_commands(app)
   # register_filters(app)
   # register_context_processors(app)

   return app

def register_blueprints(app):
   from application.frontend.views import frontend
   app.register_blueprint(frontend)


def register_extensions(app):
   from application.extensions import db
   db.init_app(app)


