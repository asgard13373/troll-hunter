import tensorflow as tf
import tensorflow_text as tf_text # dont remove it: need for downloading from hub
import tensorflow_hub as hub

RUSSIAN = 'ru'
RUSSIAN_WORDS_EMBEDDING_HUB_MODEL = 'https://tfhub.dev/google/wiki40b-lm-{}/1'.format(RUSSIAN)


def create_wiki40_russian_embedding_layer():
    return hub.KerasLayer(
        handle=RUSSIAN_WORDS_EMBEDDING_HUB_MODEL,
        signature='word_embeddings', # модель умеет многое, но нас интересует только векторизация слов
        output_key='word_embeddings',
        dtype=tf.string,
        trainable=False, # impossible to finetuned (because it is tf1 model)
        name='wiki40b'
    )
