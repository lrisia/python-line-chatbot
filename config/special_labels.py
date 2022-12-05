import config

__config = config.Config('special_labels', path='src\json\\', filename='data')

SPECIAL_LABEL=__config

GET=lambda key: __config.get(key)
"""Get special label by key"""