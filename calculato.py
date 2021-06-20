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
   import streamlit as st
   st.title('Welcome to BMI Calculator')
   weight = st.number_input("Enter your weight (in kgs)")
   status = st.radio('Select your height format: ',
				        ('cms', 'meters', 'feet'))
   if(status == 'cms'):
	   height = st.number_input('Centimeters')
	
	   try:
		   bmi = weight / ((height/100)**2)
	   except:
		   st.error("Enter some value of height")
		
   elif(status == 'meters'):
       height = st.number_input('Meters')
	
       try:
	  bmi = weight/(height**2)
       except:
          st.error("Enter some value of height")
		
      else:
	# take height input in feet
	       height = st.number_input('Feet')
	
	# 1 meter = 3.28
	       try:
		       bmi = weight / (((height/3.28))**2)
	       except:
		       st.error("Enter some value of height")

# check if the button is pressed or not
      if(st.button('Calculate BMI')):
	      st.text("Your BMI Index is {}.".format(bmi))
	
	# give the interpretation of BMI index
	      if(bmi < 16):
		      st.error("You are Extremely Underweight")
	      elif(bmi >= 16 and bmi < 18.5):
		       st.warning("You are Underweight")
	      elif(bmi >= 18.5 and bmi < 25):
		        st.success("Healthy")		
	      elif(bmi >= 25 and bmi < 30):
		        st.warning("Overweight")
	      elif(bmi >= 30):
		        st.error("Extremely Overweight")

