import streamlit as st

st.markdown(f"あなたのプログラミング経験について当てはまるものをお選びください。")
st.radio("aa", ('経験なし', '歴1年ほど', '歴2~3年ほど','歴3年以上or業務で扱っている'))


from streamlit_key2 import my_component

value = my_component()


st.markdown(f"You've typed {value}")