
from kakou import *
import pickle

WV_FILE = 'key_word2vec.bin'
MODEL_NAME = '221130_takky_random.sav'

if __name__ == '__main__':

    inputs = 's 239 SPACE 167 i 180 n 238 SPACE 172 Shift 1144 "" 244 a 248 b 385 c 214 d 397 e 313 f 251 g 153 Shift 238 "" 213 Shift'
    averaging_data = input_kakou(WV_FILE, inputs)
    averaging_data = averaging_data.reshape(1, -1)

    loaded_model = pickle.load(open(MODEL_NAME, 'rb'))
    result = loaded_model.predict(averaging_data)

    print(f'あなたは…{result}')
