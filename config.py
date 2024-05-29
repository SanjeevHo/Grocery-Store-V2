class Config(object):
    DEBUG = False
    TESTING =False
    CACHE_TYPE="RedisCache"
    CACHE_DEFAULT_TIMEOUT = 300

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SECRET_KEY = "HELLOSECRET_KEY" #whenever you are using a session you have to used secret key, flask login uses session
    SECURITY_PASSWORD_SALT = "thisissaltt" # used for encrypting a password
    SQLALCHEMY_TRACK_MODIFICATIONS =False
    WTF_CSRF_ENABLED =False # request from legitmate fornted
    SECURITY_TOKEN_AUTHENTICATION_HEADER ="Authentication-Token" # it says that header which will be accpeted is authnetication token
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 3
    


