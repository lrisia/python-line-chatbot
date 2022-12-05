import config

__config = config.Config('answers', path='src\json\\', filename='data')

ANSWER=__config

GET=lambda key: __config.get(key)
"""Get answer by key"""