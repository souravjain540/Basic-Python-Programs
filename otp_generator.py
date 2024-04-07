import os
import math
import random
import smtplib
digits = "012456789"
OTP = ""
for i in range(4):
     OTP += digits[math.floor(random.random() * 10)]
msg =  str(OTP) + "Your OTP is" 
 
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

emailid = "receiver's id"
s.login("sender's id", "google app password")
s.sendmail("sender's id", emailid, msg)
a = input("Enter the OTP >>: ")
if a == OTP:
    print("Verified")
else:
        print("Incorrect OTP")
s.quit()
