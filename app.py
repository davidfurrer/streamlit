import streamlit as st
import requests


st.header('Streamlit test app')

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)



st.header('chuck norris jokes')

if st.button('tell me a chuck norris joke'):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    st.write(response.json()['value'])


