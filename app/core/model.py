import app.configuration as config
import tensorflow as tf
import numpy as np

from gensim.models import KeyedVectors
from pythainlp.tokenize import word_tokenize
from tensorflow.keras.preprocessing.sequence import pad_sequences
from app.linebot import message_builder as MessageBuilder
from app.core.model_interface import ModelInterface
from app.core.file_handle import FileHandle

class Model(ModelInterface):
    """Handle all thing about model"""

    def __init__(self) -> None:
        """__init__ method
        

        """
        
        super().__init__(sorted(config.label.ANSWER_DICT,))
        self.word2vec_model = self.__load_word2vec_model(config.model.WORD2VEC_PATH)
        
        self.special_class = config.label.SPECIAL_CLASS_DICT
        self.image_map = config.label.IMAGEMAP_DICT

    # overwritemethod
    def _load_model(self):
        return tf.keras.models.load_model(config.model.PATH)
        # pass

    # overwritemethod
    def predict(self, text: str):
        text = text.lower().strip()
        if text in self.image_map:
            return self.__imagemap(text)
        
        vec_text, word_token = self.__text_transform(text)
        logit = self.model.predict(vec_text, batch_size=32, verbose=0)
        conf = [ logit[0][pred] for pred in np.argmax(logit, axis=1) ][0]
        predicted = [ sorted(self.label_list)[pred] for pred in np.argmax(logit, axis=1) ][0].lower()
        return predicted

        
    def __load_word2vec_model(self, path: str):
        return KeyedVectors.load_word2vec_format(path, binary=True, unicode_errors='ignore')

    def __imagemap(self, text: str) -> dict:
        content = self.image_map[text]
        try:
            path = content['path']
            preset = FileHandle().read_file(path, 'json')
            return MessageBuilder.ImagemapBuilder(preset=preset).build()
        except:
            return MessageBuilder.MessageBuilder(content).build()

    def __text_transform(self, text: str):
        stopwords = FileHandle().read_file('src/json/stop_words', 'txt')
        word_token = self.__clean_input(text, stopwords)
        word_indices = self.__map_word_index(word_token)
        length = self.model.layers[0].output_shape[0][1]
        padded_word_indices = pad_sequences([word_indices], maxlen=length, value=0)
        return [padded_word_indices, word_token]

    def __map_word_index(self, word_seq: list):
        indices = []
        for word in word_seq:
            if word in self.word2vec_model.vocab:
                indices.append(self.word2vec_model.vocab[word].index + 1)
            else:
                indices.append(1)
        return indices

    def __clean_input(self, text: str, stopwords: list):
        input_text = word_tokenize(text, keep_whitespace=False)
        list_word_not_stopwords = [i for i in input_text if i not in stopwords]
        return list_word_not_stopwords
