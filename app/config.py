class Config(object):
	SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/britecore"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False