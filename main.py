import streamlit as st
import requests

nasa_api_key = 'SavxxBtqttZre5Leu3HwbKQ5QVM5HDTTPpDFGe3d'
query = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'

response = requests.get(query)

response = response.json()

photo_url = response['url']
title = response['title']
explanation = response['explanation']


with open('image.jpg', 'wb') as photo:
    photo_response = requests.get(photo_url)
    photo.write(photo_response.content)

st.markdown(f"<h1 style='text-align: center'>{title}</h1>", unsafe_allow_html=True)
st.image('image.jpg')
st.write(explanation)




