import streamlit as st

st.title('divisor finder app')

s= int(st.number_input('Enter the number:'))

if st.button('find divisor'):
    st.write('Divisor are:')
    
    for i in range (1,s+1):

        if s%i==0:
            st.write(i)

