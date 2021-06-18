import streamlit as st
import os
st.page_title="Laptop information"
st.title("Laptop and Desktop details")
st.text_input("Your laptop's or Desktop's model")
st.text_input("Your email address so that we can tell you some compatible SSD and DRAMS")

try:
   os.mkdir("C:\\ansh_scanner")
except:
   print(" ")

from PIL import Image
#img = Image.open("C:\\Users\\erroh\\lap_img.png")
#img1 = Image.open("C:\\Users\\erroh\\Desktop_img.png")
  
# display image using streamlit
# width is used to set the width of an image
#st.image(img, width=200)
#st.image(img1, width=200)
sys=st.button("System details")
ssd=st.button("SSD info")
ram=st.button("Ram info")
battery=st.button("Battery_info")
if sys:
   try:
      os.system("Systeminfo > C:\\ansh_scanner\\system.txt")
      st.write("saved at C:\\ansh_scanner\\system.txt")
   except:
      print(" ")
if ssd:
   try:
      os.system("powershell get-physicaldisk> C:\\ansh_scanner\\SSD_Health.txt")
      st.info("saved at C:\\ansh_scanner\\SSD_Health.txt")
   except:
      print(" ")
if ram:
   try:
      os.system("wmic MemoryChip get Banklabel, Capacity, Configuredclockspeed, Devicelocator, FormFactor, Manufacturer, partnumber,Serialnumber, Speed > C:\\ansh_scanner\\Ram_info.txt")
      st.info("saved at C:\\ansh_scanner\\Ram_info.txt")
   except:
      print(" ")
if battery:
   try:
      os.system("powercfg /batteryreport")
      st.info("saved at Battery-report.html")
   except:
      print(" ")
a=st.title("Developer-Ansh Sharma")
#if a:
  #  os.system("streamlit run C:\\Users\\erroh\\Streamlit_folder\\ansh.py")
    
