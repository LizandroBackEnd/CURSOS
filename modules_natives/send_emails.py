from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText  
import smtplib
 
message = MIMEMultipart() 
message["from"] = "Lizandro" 
message["to"] = "lizandroantoniosantos@gmail.com" 
message["subject"] = "This is a test" 
body = MIMEText("Message body") 
message.attach(body) 
 
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp: 
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login("lizandroantoniosantos@gmail.com", "password") 
    smtp.send_message(message)