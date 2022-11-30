# import pickle
# filename = '221130_takky_random.sav'
# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, y_test)
# print(result)

import streamlit as st
from streamlit_key2 import my_component
import json
import pickle
import sklearn


# labels = {'0':'経験なし','1':'歴1年ほど','2':'歴2~3年ほど','3':'歴3年以上or業務で扱っている'}



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
data = value[idx1+1:]#Eisu 414 p 299 r 115 i 169 n 126 t

def head_cleansing(s):
  str_list = s.split()
  return " ".join(str_list[2:])

df_keys['keys'] = df_keys['keys'].apply(head_cleansing)



print(data)


#予測
# filename = '221130_takky_random.sav'
# loaded_model = pickle.load(open(filename, 'rb'))
# y_pred = loaded_model.predict(data)
# print(y_pred[0])


pred = 1 #結果

#結果を表示
if pred == 0:
    st.write("頑張りましょう！")
elif pred == 1:
    st.write("よくできました")
elif pred == 2:
    st.write("大変よくできました")
elif pred == 3:
    st.write("素晴らしい")