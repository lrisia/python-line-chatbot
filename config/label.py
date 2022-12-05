import config

__config = config.Config('labels', path='src\json\\', filename='data')

LABEL=__config

GET=lambda key: __config.get(key)
"""Get label by key"""