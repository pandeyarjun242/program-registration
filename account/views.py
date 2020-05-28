from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Player
import smtplib
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
import string
# Create your views here.
class Home(APIView):
    def get(self,request):
        return render(request, 'home.html')
class Signup(APIView):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self,request):
            try:
                if len(request.POST['mobile']) == 10:
                    pass
                else:
                    return render(request,'signup.html', {"error": "Please enter a valid Phone Number"})
            except:
                pass
            try:
                validate_email(request.POST['email'])
            except:
                return render(request,'signup.html', {"error": "Please enter a valid email ID"})
            try:
                email = Player.objects.get(email = request.POST['email'])
                return render(request, 'signup.html', {"error":"Account already exists from this Email ID"})
            except:
                pass
            try:
                num = player.objects.get(request.POST['mobile'])
                return render(request, 'signup.html', {"error":"Account already exists from this Mobile Number"})
            except:
                pass
            name = request.POST['name']
            email = request.POST['email']
            cityPreference = request.POST['cityPreference']
            message = request.POST['message']
            mobile = request.POST['mobile']
            profile = Player(name = name, email = email, mobile = mobile, age = 15, description =message, cityPreference = cityPreference)
            finm = "Hi "+name+"\n\nWe are thrilled to let you know that you have been registered into India's first Trans Football Program. We have a lot of exciting stuff coming up! Stay tuned for more and let's rid the football ground of cis-sexist biases together.\n\nThe program is the brainchild of ScoutMe, The Keshav Suri Foundation and Bhaichung Bhutia Football Schools. Be sure to give us your support on social media \n\nBest,\nArjun Pandey\nFounder at ScoutMe"
            msg = MIMEMultipart()
            msg['From'] = "arjun@scoutme.in"
            msg['To'] = email
            msg['Subject'] = 'Registration - Complete'
            msg.attach(MIMEText(finm,'plain'))
            text = msg.as_string()
            profile.save()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            newmsg = MIMEMultipart()
            newmsg['From'] = "arjun@scoutme.in"
            newmsg['To'] = "arjun@scoutme.in"
            newmsg['Subject'] = 'registered'
            n =  "\nEmail - "+email+"\nMobile- "+mobile +"\nMessage - " + message + "\nCity - "+cityPreference
            newmsg.attach(MIMEText(n,'plain'))
            newtext = newmsg.as_string()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('pandeyarjun.242@gmail.com', 'arjun2003')
            server.sendmail('pandeyarjun.242@gmail.com',[email],text)
            server.sendmail('pandeyarjun.242@gmail.com',["arjun@scoutme.in"],newtext)
            server.quit()
            return render(request, 'aftersignup.html',{"error":"Your account has been created!"})
class Contact(APIView):
    def get(self, request):
        return render(request, 'contact.html')
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        rec = [email]
        userm =  "Hi "+name+"\n\nThank you for your query! We will be reaching out to you in the next 3 days.\n\nStay tuned for more! \n\nBest,\nThe Kicking Gender Boundaries Team"
        msg = MIMEMultipart()
        msg['From'] = "arjun@scoutme.in"
        msg['To'] = email
        msg['Subject'] = 'Contact Query'
        msg.attach(MIMEText(userm,'plain'))
        text = msg.as_string()
        # Hello
        mym = "Name - "+name+"\nEmail - "+email+"\nSubject - "+subject+"\nMessage - "+message
        newmsg = MIMEMultipart()
        newmsg['From'] = "arjun@scoutme.in"
        newmsg['To'] = "arjun@scoutme.in"
        newmsg['Subject'] = 'Contact Query'
        newmsg.attach(MIMEText(mym,'plain'))
        newtext = newmsg.as_string()
        #Gaps for convenience
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('pandeyarjun.242@gmail.com', 'arjun2003')
        server.sendmail('pandeyarjun.242@gmail.com',rec,text)
        server.sendmail('pandeyarjun.242@gmail.com',["arjun@scoutme.in"],newtext)
        server.quit()
        return redirect('home')
