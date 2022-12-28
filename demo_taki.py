import streamlit as st
from streamlit_key2 import my_component
import json
import pickle
from kakou import *
from PIL import Image
from datetime import datetime

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
# st.write("あなたのプログラミング経験について当てはまるものを１つお選びください。")
# streamlit.write(<TAG style="hoge:bar">ホゲホゲ</TAG>, unsafe_allow_html=True)

# st.write(<h2>あなたのプログラミング経験について当てはまるものをお選びください。</h2>, unsafe_allow_html=True)
year = st.radio(label = "あなたのプログラミング経験について当てはまるものをお選びください", 
    options = ("経験なし", "半年~2年ほど", "3年以上or業務で扱っている"))

# st.markdown('<div style="margin:20px; border-top: solid 4px gray;"><p style="padding: 40px 0 10px 0; text-align:center;">右側の水色枠内に、左側のお手本と同じコードをタイプしてください！<br>すべてのコードをタイプし終えたら、完了ボタンを押してください。</p></div>', unsafe_allow_html=True)

st.markdown('<p style="padding: 40px 0 10px 0; text-align:center; margin:20px; border-top: solid 4px gray;">右側の水色枠内に、左側のお手本と同じコードをタイプしてください！<br>すべてのコードをタイプし終えたら、完了ボタンを押してください。</p>', unsafe_allow_html=True)


#キータイピングデータ取得
data = my_component()
labels = {"経験なし":0,"歴1~2年ほど":1,"歴3年以上or業務で扱っている":2}
date = str(datetime.now().date())
date_time = str(datetime.now())

if data == "":
    pass
else:
    #キータイピングデータの表示
    # st.markdown('<h1>Hello</h1>', unsafe_allow_html=True)

    #ログデータ回収
    with open('keylog.jsonl', 'a') as f:
        dataset = {'label':labels[str(year)], 'data':data,'date':date,'datetime':date_time}#{"year":"経験なし","value":"5742 p 166 r 101 i 149 n 132 t"}
        json.dump(dataset, f, separators=(',',':'),ensure_ascii=False)
        f.write('\n')
    
    #キーターピングレベルの表示
    result = typing_level(data)
    # print(result)
    # image_1 = Image.open('results_2.png')
    # <p><img src="sample.jpg" alt="サンプル画像"></p>
    # st.markdown('<p><img src="results_2.png" alt="サンプル画像"></p>', unsafe_allow_html=True)
    # st.image(image_1)

    if result == 0:
        image_1 = Image.open('results_1.png')
        st.image(image_1)
        st.markdown('<p style="padding: 10px 0 10px 0; text-align:center;">ご協力いただきありがとうございます！</p>', unsafe_allow_html=True)

    elif result == 1:
        image_2 = Image.open('results_2.png')
        st.image(image_2)
        st.markdown('<p style="padding: 10px 0 10px 0; text-align:center;">ご協力いただきありがとうございます！</p>', unsafe_allow_html=True)

    elif result == 2:
        image_3 = Image.open('results_3.png')
        st.image(image_3)
        st.markdown('<p style="padding: 10px 0 10px 0; text-align:center;">ご協力いただきありがとうございます！</p>', unsafe_allow_html=True)

    else:
        image_4 = Image.open('results_4.png')
        st.image(image_4)
        st.markdown('<p style="padding: 10px 0 10px 0; text-align:center;">ご協力いただきありがとうございます！</p>', unsafe_allow_html=True)




    
