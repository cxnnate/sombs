'''
Configurations for streaming tweets from Twitter
'''

config = {
    'production': {
        'host': '0.0.0.0',
        'port': 80,
        'debug': False,
        'clear_db': False,
        'postgres': {
            'name': 'database',
            'user': 'admin',
            'password': 'password',
            'host': 'database',
            'port': 5432
        }
    }, 

    'development': {
        'host': 'localhost',
        'port': 8080,
        'debug': True,
        'clear_db': False,
        'postgres': {
            'name': 'database',
            'user': 'admin',
            'password': 'password',
            'host': 'localhost',
            'port': 5432
        }
    }
    'twitter_consumer_key': '3ZvlZXSt61mKScLZN1RPO0R6R', 
    'twitter_consumer_secret': 'TbqFhWxQ7hncXTB7XAeA4QjvLg7FkWXmMxjsM2AOMTOqTRCjyG', 
    'twitter_access_key': '1163449515615105026-86ELYUGZtvkmAJ35wD1kJecsLMDjUz', 
    'twitter_access_secret': 'PvCnJF6aqhr5Xser7IjlprqD4ZDTnKbvDOMyu9VV6cCTr'
}