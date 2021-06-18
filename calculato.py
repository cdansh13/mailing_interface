import streamlit as st
st.title("Calculator-Ansh Sharma")
st.header("This calculator can do Addition")
a=st.number_input("1st no.")
b=st.number_input("2nd no.")
c=st.button("Add")
if c:
   st.write(a+b)
