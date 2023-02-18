import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'secret'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite://'
	WTF_CSRF_ENABLED = False
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'data/sqlite')

	@classmethod
	def init_app(cls, app):
		Config.init_app(app)

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	
	'default': DevelopmentConfig
} 