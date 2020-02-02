import os


class Config:
    SQLALCHEMY_DATABASE_URI = \
        'postgresql+{driver}://{user}:{password}@{host}:{port}/dbname'.format(
            driver='psycopg2', user=os.getenv('FLASK_DB_USER', 'postgres'),
            password=os.getenv('FLASK_DB_PASS'),
            host=os.getenv('FLASK_DB_HOST', 'localhost'),
            port=os.getenv('FLASK_DB_PORT', 5432),
            dbname=os.getenv('FLASK_DB_DBNAME', 'postgres')
        )


class DevelopmentConfig(Config):
    MODE = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class StagingConfig(Config):
    MODE = 'stg'
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    MODE = 'prov'
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_map = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
