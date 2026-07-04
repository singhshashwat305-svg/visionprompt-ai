import streamlit as st
st.title ('Subbtraction app')

n1= st.number_input('Enter number n1:')
n2 = st.number_input('Enter number n2:')

if st.button('subtract'):
    c=n1-n2
    st.success(f'the subtraction of {n1} and {n2} is {c}')

