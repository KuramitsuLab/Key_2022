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
#inputs = 's 239 SPACE 167 i 180 n 238 SPACE 172 Shift 1144 "" 244 a 248 b 385 c 214 d 397 e 313 f 251 g 153 Shift 238 "" 213 Shift'
str_list = value.split()
inputs = " ".join(str_list[2:])
if inputs == "":
    pass
else:
    averaging_data = input_kakou(WV_FILE, inputs).reshape(1, -1)

    #予測
    filename = '221130_takky_random.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(averaging_data)
    #結果を表示
    st.write(result) 
