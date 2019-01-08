"""Configuration files for the API"""


class Config(object):
    """Parent configuration class"""

    DEBUG = False
    SECRET_KEY = "pleasedontguess"
    ENV = "development"
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    """configurations for development environment"""

    DEBUG = True


class TestingConfig(Config):
    """configurations for testing environment"""

    DEBUG = True


class StagingConfig(Config):
    """configurations for staging environment"""

    DEBUG = True


class ProductionConfig(Config):
    """configurations for production environment"""

    DEBUG = False


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}

secret_key = Config.SECRET_KEY
