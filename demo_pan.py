import streamlit as st
from streamlit_key2 import my_component
import json
import pickle
from kakou import *

#キーターピングレベル診断
def typing_level(ss):
    #入力データ作成
    WV_FILE = 'key_word2vec.bin'
    ss_list = ss.split()
    inputs = " ".join(ss_list[2:])
    inputs = input_kakou(WV_FILE, inputs).reshape(1, -1)

    #予測
    modelname = '221130_takky_random.sav'
    loaded_model = pickle.load(open(modelname, 'rb'))
    result = loaded_model.predict(inputs)[0]
    
    return result


#アンケート
year = st.radio(label = "あなたのプログラミング経験について当てはまるものをお選びください。", 
    options = ('経験なし', '歴1年ほど', '歴2~3年ほど','歴3年以上or業務で扱っている'))


#キータイピングデータ取得
data = my_component()

if data == "":
    pass
else:
    #キータイピングデータの表示
    st.markdown(f"You've typed {data}")

    #ログデータ回収
    with open('keylog.jsonl', 'a') as f:
        dataset = {'year':year, 'data':data}#{"year":"経験なし","value":"5742 p 166 r 101 i 149 n 132 t"}
        json.dump(dataset, f, separators=(',',':'),ensure_ascii=False)
        f.write('\n')
    
    #キーターピングレベルの表示
    result = typing_level(data)#0
    st.write(result)
    
