import streamlit as st

st.header('streamlit test app')

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)