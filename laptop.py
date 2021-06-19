import streamlit as st
import os
try:
   os.mkdir("C:\\ansh_scanner")
except Exception as e:
   st.error(e)
st.title("Laptop Desktop info")
st.subheader("Just download this file and it would be saved in C:\\ansh_scanner")
down=st.button("Download")
if down:
   try:
     f = open("C:\\ansh_scanner\\laptop_detail.bat", "a")
     f.write("python C:\\Users\\erroh\\laptop_recovery.py")
     f.close()
     st.success("Saved at C:\ansh_scanner\laptop_detail.bat")
   except:
     psss
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
