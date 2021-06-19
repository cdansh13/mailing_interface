# import module
import streamlit as st

# traverse the infoimport streamlit as st
st.title("Calculator-Ansh Sharma")
st.header("This is a website which will help you in doing arithmatic operations")
a=st.number_input("1st no.")
b=st.number_input("2nd no.")
addi=st.button("Addition")
subt=st.button("Subtraction")
mull=st.button("Multiplicatin")
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
if myself:
   try:
      import webbrowser
      webbrowser.open("https://share.streamlit.io/cdansh13/mailing_interface/main/c.py")
   except Exception as e:
      st.error(e)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
