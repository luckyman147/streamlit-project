import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()



col1, col2, col3 = st.columns(3)
col2.image(Image.open('img.png'))

st.header('Iyed Touati')

st.info('Data scientist, Machine Learning engineer')

icon_size = 20

st_button('github', 'https://github.com/luckyman147','Come see My projects',icon_size)
st_button('facebook', 'https://www.facebook.com/iyed.touati.432002', 'Follow me on Facebook', 20)

st_button('linkedin', 'https://www.linkedin.com/in/iyed-touati-41a088226/', 'Follow me on LinkedIn', icon_size)
