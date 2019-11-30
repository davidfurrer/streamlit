# streamlit

## usage

```
streamlit run app.py
```

## deploy to Heroku

```
heroku login && heroku create && git push heroku master && heroku ps:scale web=1 && heroku open
```