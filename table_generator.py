import streamlit as st
st.title('Table generator app')

a= int(st.number_input('Enter the number for which you want to generate the table:'))

if st.button('Generate table'):
    st.write("table is:")
    for i in range(1,11):
        st.write(f'{a}x{i}={a*i}')
    