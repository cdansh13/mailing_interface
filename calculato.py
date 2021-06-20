# import module
import streamlit as st
choice=st.sidebar("Calculator","BMI calculator")
# traverse the infoimport streamlit as st
st.title("This app will help you in doing Simple Calculations and in Finding BMI")
if choice=="Calculator": 
   st.header("Calculator-Ansh Sharma")
   st.header("This is tab will help you in doing arithmetic operations")
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
   myself=st.header("Developer-Ansh Sharma")
   st.write("Youtube channel of Ansh Sharma: https://www.youtube.com/channel/UC4_ViKxs-QmPx2NTPhdkBDw")
   hide_streamlit_style = """
   <style>
   #MainMenu {visibility: hidden;}
   footer {visibility: hidden;}
   </style>
   """
   st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
if choice=="BMI calculator":
   # import the streamlit library
   import os
   os.system("C:\\Users\\erroh\\Streamlit_folder\\BMI_calculator.py")

