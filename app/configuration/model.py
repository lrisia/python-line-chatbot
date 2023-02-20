from app.configuration import config

__config = config.Config('model')

CONF=__config.get('conf')

PATH=__config.get('path')

WORD2VEC_PATH=__config.get('word2vec')