
import streamlit as st
import pandas as pd

st.title("Lets emojify the text")


text=st.text_input('Enter some text')
st.checkbox('Check me out')
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])

st.slider('Slide me', min_value=0, max_value=10)

st.write("🙂",text.lower())
st.button('Click-here')