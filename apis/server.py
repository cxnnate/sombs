import os
import json
import time
import boto3

from config import config
from flask import Flask, request
# from logging.config import dictConfig
from src import Twitter

def create_application():
    """
    Initialize Flask application

    :return: new Flask application
    """

    # dictConfig({
    #     'version': 1,
    #     'formatters': {
    #         'default': {
    #             'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #         }
    #     },
    #     'handlers': { 'wsgi': {
    #         'class': 'logging.StreamHandler',
    #         'stream': 'ext://flask.logging.wsgi_errors_stream',
    #         'formatter': 'default'
    #     }},
    #     'root': {
    #         'level': 'DEBUG' if os.getenv('DEBUG', False) else 'INFO',
    #         'handlers': ['wsgi']
    #     }
    # }) 

    application = Flask(__name__, static_url_path=None)
    application.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(32))

    env = os.getenv('ENVIRONMENT', 'production')
    application.logger.info('env')
    application.config['ENV'] = env
    application.config['DEBUG'] = os.getenv('DEBUG', config[env]['debug'])

    # s3_bucket = boto3.client('s3')
    def get_s3_bucket():
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('sombs-api-keys')
        return bucket

    # main route
    @application.route("/")
    def index():
        message = "Running up the Social Media API component..."
        application.logger.debug(message)
        return message
    
    @application.before_first_request
    def before_first_request():
        application.logger.info("Establishing database connection...")

    @application.route("/start_twitter_stream", methods=['POST', 'GET'])
    def start_twitter_stream():
        """
        Endpoint to start streaming live tweets from Twitter. Requires a list of topics, stream duration,
        :param topics:
        :param duration:
        :return:
        """
        
        # get twitter API keys from S3 bucket
        s3_bucket = get_s3_bucket()
        for obj in bucket.objects.all():
            key = obj.key
            body = obj.get()['Body'].read()
            print(key, body)
        
        # create ID for stream (want to start stream thread)

        return "", 200

    @application.route("/stop_twitter_stream", methods=['POST'])
    def stop_twitter_stream():
        """
        Endpoint to stop streaming live tweets from Twitter. Requires a list of topics, stream duration,
        :param topics:
        :param duration:
        :return
        """
        print("brap brap stop", flush=True)
        return "", 200
    
    return application


if __name__ == "__main__":
    application = create_application()
    application.run("0.0.0.0", 80)