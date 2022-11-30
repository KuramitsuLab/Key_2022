import streamlit as st
st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))
from streamlit_key import my_component

value = my_component('Hi')
st.markdown(f"You've typed {value}")

