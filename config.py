

class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    LEGACY_DB_URI = "http://localhost:5007"
    MQ_USERNAME = "mquser"
    MQ_PASSWORD = "mqpassword"
    MQ_HOSTNAME = "localhost"
    MQ_PORT = "5672"


class PreviewConfig(Config):
    LEGACY_DB_URI = "http://localhost:5007"
    MQ_USERNAME = "mquser"
    MQ_PASSWORD = "mqpassword"
    MQ_HOSTNAME = "localhost"
    MQ_PORT = "5672"