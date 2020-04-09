import os

# 388483424:AAFnlNhu6tuIovFM-fBVEXxlFG9le829IwA
def get_token():
    token = os.environ.get('BOT_TOKEN')
    if not token:
        token = '1114300376:AAFr93tXigLcSNVQZjbF9rZumlcSuRaLIxI'
    return token


greeting_message = '''
Welcome to location bot!

/add - to add a new place. i.e. /add 100 King street west
/list - to see a list of saved locations.
/reset - to clear all saved locations and start fresh.

Enjoy!
'''


def save_address(user_id, address):
    pass

