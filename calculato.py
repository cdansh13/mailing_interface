import streamlit as st
import os
#try:
 #  os.mkdir("C:\\A")
#except:
   #print("sorry")
a=st.button("Laptop/Desktop information")
if a:
   os.system('cmd /c"systeminfo"')
