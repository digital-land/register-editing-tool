import os


class Config:
    CONFIG_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(CONFIG_ROOT, os.pardir))
    SECRET_KEY = os.getenv('SECRET_KEY')
    SCHEMA_URL = os.getenv('SCHEMA_URL')
    SCHEMA_API_URL = os.getenv('SCHEMA_API_URL')

class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    pass