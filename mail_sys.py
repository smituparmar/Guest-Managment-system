import pandas as pd
import os
import time

data=pd.read_csv('data_file.csv')

f=open('final_mail.js','w')
f.write('var email 	= require("./node_modules/emailjs/email");\n')
f.write('var server 	= email.server.connect({\n')
f.write('user:    "workforsmit@gmail.com",\n') 
f.write('password:"enter-your-password",\n') 
f.write('host:    "smtp.gmail.com",\n') 
f.write('ssl:     true\n')
f.write('});\n\n')

l=len(data)
for i in range(l):
    f.write('server.send({\n')
    f.write('text: "Hey '+data['Name'][i]+'",\n') 
    f.write('from:    "workforsmit@gmail.com",\n')
    f.write('to:"'+data['email'][i]+'",\n')
    f.write('subject: "testing emailjs",\n')
    f.write('attachment:\n') 
    f.write('[\n')
    f.write('{path:"E:/testdeep/email_system/img.jpg", type:"image/jpg", name:"claire.jpg"},\n')
    f.write(']\n')
    f.write('}, function(err, message) { console.log(err || message); });\n\n')

f.close()

#print(os.system('node final_mail.js'))
time.sleep(10)
