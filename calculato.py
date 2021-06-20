# import module
import streamlit as st
menu=["Calculator","Area of Square","Area of Rectangle"]
choice=st.sidebar.selectbox("Select Operation:",menu)
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
elif choice=="Area of Square":
   # import the streamlit library
   reqe=number_input("Side of square")
   unit=st.text_input("Unit of side")
   try:
      st.write(reqe*reqe+unit+"²")
   except:
      st.error("Invalid entry")
elif choice=="Area of Rectangle":
   le=number_input("Length of Rectangle")
   b=number_input("Breadth of Rectangle")
   un=text_input("Unit of Length and Breadth")
   try:
      st.write(le*b+un+"²")
   except:
      st.error("Invalid entry")
