import streamlit as st
from streamlit_key2 import my_component
import json
import pickle
from kakou import *


#アンケート
year = st.radio(label = "あなたのプログラミング経験について当てはまるものをお選びください。", 
    options = ('経験なし', '歴1年ほど', '歴2~3年ほど','歴3年以上or業務で扱っている'))


#キーデータ収集
value = my_component()
st.markdown(f"You've typed {value}")


#ログをjsnol形式へ
with open('keylog.jsonl', 'a') as f:
    if value == "":
        pass
    else:
        dict = {'year':year, 'value':value}#{"year":"経験なし","value":"15114 p 160 r 71 i 136 n 154 t"}
        json.dump(dict, f, separators=(',',':'),ensure_ascii=False)
        f.write('\n')


#入力データ作成
idx1 = value.find(" ")
inputs = value[idx1+1:]#Eisu 414 p 299 r 115 i 169 n 126 t
averaging_data = input_kakou(WV_FILE, inputs)
averaging_data = averaging_data.reshape(1, -1)


#予測
filename = '221130_takky_random.sav'
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(averaging_data)


#結果を表示
st.write(result) 
