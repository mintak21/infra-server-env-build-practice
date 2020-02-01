class Config:
    pass


class DevelopmentConfig(Config):
    MODE = 'development'
    DEBUG = True


class StagingConfig(Config):
    MODE = 'stg'
    DEBUG = False


class ProductionConfig(Config):
    MODE = 'prov'
    DEBUG = False


config_map = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
