# SOcial Media Bot Sentiment - SoMBS

## that's some bs, right?

 The goal of the project is to understand how social spambots affect the sentiment of topics discussed on social media platforms. My aim for this project is to turn this idea into a usable web application and expand the services by implementing state-of-the-art natural language processing techiques to fight disinformation. 

## Data Collecting

Data is collected from Twitter using Tweepy. 

To start the data streaming tool, ensure Tweepy is installed

`pip install tweepy` then run,
`python3 stream.py --creds <credentials> --keys <keywords> --time 5`

Arguments
- creds: A JSON file of Twitter API credentials. Apply for one here
- keys: A file of keywords to filter the stream
- time: Time limit

## Topic Model

Search for latent topics in the data

## Sentiment Analysis

* Will be using off-the-shelf models such as VADER or NLTK Sentiment Analyzers
* eventually, will create my own sentiment analyzer using pytorch

Classify the polarity of a given tweet

## Bot Detection

Produce a bot score based on the given features


### Author
Nate

   ` "build": "npx tailwindcss --watch -i ./input.css -o ./output.css"`
