import streamlit as st
st.title("Calculator")
a=st.text_input("Your operator")
b=st.text_input("Your first number")
c=st.text_input("Your second number")
d=st.button("Done")
if d:
    if a=="+":
      ad=b+c
      st.write(ad)
    if a=="-":
      su=b-c
      st.wrte(su)
    if a=="*":
      mull=b*c
      st.write(mull)
    if a=="/":
      divide=b/c
      st.write(divide)
  
