# streamlit

## app

```python
import streamlit as st

st.header('streamlit test app')

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

```

## usage locally

```
streamlit run app.py
```

## deploy to Heroku

sign up

```
heroku login && heroku create && git push heroku master
```
Go to url shown

## result

https://aqueous-savannah-99501.herokuapp.com/

## Procfile

Specifies deployment

```
web: streamlit run app.py
```
