import streamlit ast st
import os
#try:
 #  os.mkdir("C:\\A")
#except:
   #print("sorry")
a=st.button("Laptop/Desktop information")
if a:
   os.system("systeminfo")
