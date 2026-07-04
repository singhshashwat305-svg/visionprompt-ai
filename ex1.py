import streamlit as st

st.write('my first app with streamlit')
st.title('super app')
st.header('best app')
st.text_input('name app')
a=st.number_input('Enter a number')
st.button('Click')
st.selectbox('what you want to select', ['Add', 'Subtract'])
st.checkbox('what you want to select', ['Add', 'Subtract'])
st.radio('what you want to select', ['Add', 'Subtract'])