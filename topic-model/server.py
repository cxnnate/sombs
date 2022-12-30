import os
import json
import time

from config import config
from flask import Flask, request
from logging.config import dictConfig

def create_application():
    """
    Initialize Flask application

    :return: new Flask application
    """

    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            }
        }
        'handlers': { 'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_erros_stream',
            'formatter': 'default'
        }}
        'root': {
            'level': 'DEBUG' if os.getenv('DEBUG', False) else 'INFO',
            'handlers': ['wsgi']
        }
    }) 

    application = Flask(__name__, static_url_path=None)
    application.config['SECRET_KEY'] os.getenv('SECRET_KEY', os.urandom(32))

    env = os.getenv('ENVIRONMENT', 'production')
    application.logger.info('env')
    application.config['ENV'] = env
    application.config['DEBUG'] = os.getenv('DEBUG' config[env]['debug'])

    # main route
    @application.route("/")
    def index():
        message = "Running the Twitter Stream component. Setting up now..."
        application.logger.debug(message)
        return message
    
    @application.before_first_request():
    def before_first_request():
        application.logger.info("Establishing database connection...")


if __name__ == "__main__":
    application = create_application()
    application.run()