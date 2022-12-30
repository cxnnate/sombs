"""
Configurations for streaming tweets from Twitter
"""

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
}