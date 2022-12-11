from setuptools import setup

setup(
   name='Sentiment Bot Detection',
   version='1.0',
   description='A system designed to analyze social spambot influence on topics of discussion on social media.',
   author='Connate',
   author_email='cxnnate@gmail.com',
   packages=['senti-bot-detection'],  #same as name
   install_requires=['tweepy'], #external packages as dependencies
)