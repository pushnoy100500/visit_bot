import os
import redis


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')


def get_token():
    if ENVIRONMENT == 'development':
        return '388483424:AAFnlNhu6tuIovFM-fBVEXxlFG9le829IwA'
    return os.environ.get('BOT_TOKEN')


greeting_message = '''
Welcome to location bot!

/add - to add a new place. i.e. /add 100 King street west
/list - to see a list of saved locations.
/reset - to clear all saved locations and start fresh.

Enjoy!
'''


class Storage:
    class __RedisStorage:
        def __init__(self):
            if ENVIRONMENT == 'development':
                self.connection = redis.Redis(host='localhost', port=6379, db=0)
            else:
                self.connection = redis.from_url(os.environ.get('REDIS_URL'))

        def add_address(self, user_id, address):
            self.connection.lpush(user_id, address)

        def get_address_listings(self, user_id):
            return self.connection.lrange(user_id, 0, 10)

        def reset_address_listings(self, user_id):
            self.connection.delete(user_id)

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Storage.__RedisStorage()
        return cls.instance
