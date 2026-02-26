import streamlit as st
from PIL import Image 

st.title("Esta es mi primera app en la nube")

st.header("En este espacio comienzo a desarrollar mis aplicaciones.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('cloud.jpg')
st.image(image, caption='Interfaces multimodales')
                   
texto = st.text_input('escribe algo','este es mi texto')
st.write('el texto escrito es', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Columna 1")
  st.write("abc?")
  resp = st.checkbox("123")
  if resp:
    st.write("Muy bien")
