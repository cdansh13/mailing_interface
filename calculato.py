import streamlit as st
import os
#try:
 #  os.mkdir("C:\\A")
#except:
   #print("sorry")
a=st.button('cmd /c"Laptop/Desktop information"')
if a:
   os.system("systeminfo")
