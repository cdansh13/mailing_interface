import streamlit as st
st.title("Calculator-Ansh Sharma")
st.header("This calculator can do Addition")
a=st.text_input(int("1"))
b=st.text_input(int("2"))
c=st.button("Add")
if c:
   st.write(a+b)
