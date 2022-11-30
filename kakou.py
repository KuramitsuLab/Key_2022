
import numpy as np
from gensim.models import KeyedVectors
from gensim.matutils import unitvec

WV_FILE = 'key_word2vec.bin'

def input_kakou(WV_FILE, text):
    key_wv = KeyedVectors.load_word2vec_format(WV_FILE, binary=True)
    averaging_result = averaging(key_wv, w2v_tokenize_text(text))
    return averaging_result

def w2v_tokenize_text(text):
    tokens = text.split()
    return tokens

def averaging(key_wv, words):
    mean = np.mean([key_wv .get_vector(word) for word in words if word in key_wv], axis=0)
    return unitvec(mean)

# def averaging_text(key_wv, text):
#     return averaging(key_wv, w2v_tokenize_text(text))

# def averaging_list(key_wv, text_list):
#     return [averaging_text(key_wv, text) for text in text_list]

# def wv_load_word2vec(WV_FILE):
#     key_wv = KeyedVectors.load_word2vec_format(WV_FILE, binary=True)
#     return key_wv


if __name__ == '__main__':

    tng_plot = 'm 466 a 637 t 909 h 956 . 144 s 777 i 399 n 296 Shift 735 ( 201 m 576 a 583 t 765 h 466 . 844 p'

    averaging_result = input_kakou(WV_FILE, tng_plot)

    print(averaging_result)
    print(type(averaging_result))
    print(averaging_result.reshape(1, -1))
