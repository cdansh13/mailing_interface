import streamlit as st
import os
try:
   os.mkdir("C:\\icomputer")
except:
   pass
st.title("Laptop Desktop info")
st.subheader("Just download this file and it would be saved in C:\\icomputer")
down=st.button("Download")
if down:
   try:
     f = open("C:\\icomputer\\laptop_detail.bat", "a")
     f.write("python C:\\Users\\erroh\\laptop_recovery.py")
     f.close()
     st.success("Saved at C:\icomputer\laptop_detail.bat")
   except:
     psss
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
