from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText  
from string import Template  
from pathlib import Path
import smtplib  

 

template_send = Path("./modules_natives/template.html").read_text("utf-8")
template = Template(template_send) 
body = template.substitute({"name": "Lizandro"})
 
message = MIMEMultipart() 
message["from"] = "Lizandro" 
message["to"] = "lizandroantoniosantos@gmail.com" 
message["subject"] = "This is a test" 
body = MIMEText(body, "html") 
message.attach(body) 
 
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp: 
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login("lizandroantoniosantos@gmail.com", "password") 
    smtp.send_message(message)  
    print("Sent...")
     