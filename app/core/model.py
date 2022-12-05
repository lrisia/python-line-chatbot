import configuration as config

import tensorflow as tf
from gensim.models import KeyedVectors

class Model:
    """Handle all thing about model"""

    def __init__(self) -> None:
        """__init__ method
        

        """

        self.model = self.__load_model(config.model.MODEL_PATH)
        self.word2vec_model = self.__load_word2vec_model(config.model.WORD_2_VEC_MODEL_PATH)
        self.label = sorted(self.__label_list(config.label.LABEL))
        self.special_label = self.__label_list(config.special_label.SPECIAL_LABEL)

    def __load_model(self, path: str):
        return tf.keras.models.load_model(path)

    def __load_word2vec_model(self, path: str):
        return KeyedVectors.load_word2vec_format(path, binary=True, unicode_errors='ignore')

    def __label_list(self, data: dict) -> list:
        return [i.lower() for i in list(data)]