import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import json
import time
from email.mime.text import MIMEText
from email.header import Header


url = "https://www.cvs.com/immunizations/covid-19-vaccine/immunizations/covid-19-vaccine.vaccine-status.TX.json?vaccineinfo"
status = "Fully Booked"
status1 = "Fully Booked"
status2 = "Fully Booked"
password = input()
sender_email = "please type sender email address"
port = 465  # For starttls
receiver_email1 = "please type receiver email address"

message = """\
Subject: Vaccine Available!(Houston or Katy or Sugar land)

Please see the CVS Vaccine Website.https://www.cvs.com/immunizations/covid-19-vaccine"""
while(status.lower() == "fully booked" and status1.lower() == "fully booked" and status2.lower() == "fully booked"):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    site_json=json.loads(soup.text)
    data = site_json.get('responsePayloadData').get('data').get('TX'); # you can change to any state abbreviation
    for d in data:
        if d.get('city').lower() == 'houston':  # change to the city name you like
            status = d.get('status')
        if d.get('city').lower() == 'katy':  # change to the city name you like
            status1 = d.get('status')
        if d.get('city').lower() == 'sugar land':  # change to the city name you like
            status2 = d.get('status')
    print("Houston: " + status)
    print("Katy: " + status1)
    print("Sugar Land: " + status2)

    if status.lower() == "fully booked" and status1.lower() == "fully booked" and status2.lower() == "fully booked":
        pass
    else:
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
             server.login(sender_email, password)
             server.sendmail(sender_email, receiver_email1, message)
        print("succed")
    time.sleep(30)

