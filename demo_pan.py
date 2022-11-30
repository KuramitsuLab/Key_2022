import streamlit as st
from streamlit_key2 import my_component
import json

#アンケート
st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))


#キーデータ収集
value = my_component()
st.markdown(f"You've typed {value}")


#ログをjsnol形式へ
with open('keylog.jsonl', 'a') as f:
    f.write(value)
    f.write('\n')


#モデルの入力作成


#予測


#結果を表示


