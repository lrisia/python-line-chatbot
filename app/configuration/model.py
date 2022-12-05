from configuration import config

__config = config.Config('model')

MODEL_CONF=__config.get('conf')

MODEL_PATH=__config.get('path')

WORD_2_VEC_MODEL_PATH=__config.get('word2vec')