import streamlit as st
st.title('Addition app')

a=st.number_input('Enter the first number')
b=st.number_input('Enter the second number')

if st.button('Add'):
    c= a+b
    st.success(f'the addition of {a} and {b} is: {c}')