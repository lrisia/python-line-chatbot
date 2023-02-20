from app.configuration import config

__PATH = 'src/json'
__FILENAME = 'data'

__config_label = config.Config('labels', path=__PATH, filename=__FILENAME)
__config_answer = config.Config('answers', path=__PATH, filename=__FILENAME)
__config_special = config.Config('special_labels', path=__PATH, filename=__FILENAME)
__config_imagemap = config.Config('image_message', path=__PATH, filename=__FILENAME)



ANSWER_DICT=__config_answer.get_all()
SPECIAL_CLASS_DICT=__config_special.get_all()
IMAGEMAP_DICT=__config_imagemap.get_all()

GET_ANSWER=lambda *key: __config_answer.get(key)
"""Get label by key"""