# import module
import streamlit as st

# traverse the infoimport streamlit as st
st.title("Calculator-Ansh Sharma")
st.header("This is a website which will help you in doing arithmatic operations")
a=st.number_input("1st no.")
b=st.number_input("2nd no.")
addi=st.button("Addition")
subt=st.button("Subtraction")
mull=st.button("Multiplication")
divide=st.button("Division")
if addi:
   st.write(a+b)
if subt:
   st.write(a-b)
if mull:
   st.write(a*b)
if divide:
   st.write(a/b)
st.header("Developer-Ansh Sharma")
#st.video("C:\\Users\\erroh\\Pictures\\Camera Roll\\calc.mp4")
