import streamlit as st
st.title("My mailing interface-Ansh Sharma")
user=st.text_input("Your email address")
pas=st.text_input("Your password")
rec=st.text_input("Reciever email address")
mes=st.text_area("Message")
a=st.button("Send")
if a:
      import smtplib
      smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
      smtpobj.starttls()
      senderemail_id=user
      senderemail_id_password=pas
      receiveremail_id=rec
# Authentication for signing to gmail account
      smtpobj.login(senderemail_id, senderemail_id_password)#cdansh13@gmail.com python@13 errohit79@gmail.com
# message to be sent
      message =mes
# sending the mail - passing 3 arguments i.e sender address, receiver address and the message
      smtpobj.sendmail(senderemail_id,receiveremail_id, message)
# Hereby terminate the session
      smtpobj.quit()
      st.write("sent")
