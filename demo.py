import streamlit as st
st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))
from streamlit_key22 import my_component

value = my_component()

st.markdown(f"You've typed {value}")

