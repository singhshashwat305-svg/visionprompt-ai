import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

st.header('Image analytics')

uploaded_file=st.file_uploader('Upload an image',type=['png','jpg','jpeg'])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file))

prompt=st.text_input('Enter the text')


if st.button('GET RESPONSE'):
    img=Image.open(uploaded_file)
    model=genai.GenerativeModel('models/gemini-2.5-flash')
    response=model.generate_content([prompt,img])
    st.markdown(response.text)

