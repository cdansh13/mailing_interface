# import module
import streamlit as st
menu=["Calculator","Area of Square","Area of Rectangle"]
choice=st.sidebar.selectbox("Select Operation:",menu)
# traverse the infoimport streamlit as st
st.title("This app will help you in doing Simple Calculations and in Finding Areas of Square and Rectangle")
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
elif choice=="Area of Square":
   st.header("This tab will help you in finding the _Area_ of _Square_")
   # import the streamlit library
   reqe=st.number_input("Side of square")
   unit=st.text_input("Unit of side")
   fin=st.button("Done")
   if fin:
      try:
         st.write(reqe*reqe,unit,"²")
      except Exception as e:
         st.error(e)
elif choice=="Area of Rectangle":
   st.header("This tab will help you in finding the _Area_ of _Rectangle_")
   le=st.number_input("Length of Rectangle")
   b=st.number_input("Breadth of Rectangle")
   un=st.text_input("Unit of Length and Breadth")
   fk=st.button("Done")
   if fk:
      try:
         st.write(le*b,un,"²")
      except Exception as l:
         st.error(l)
