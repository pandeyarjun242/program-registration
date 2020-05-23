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
            # emailm = EmailMessage('Registration Complete!',"Hi "+name+"\n\nWe are thrilled to let you know that you have been registered into India's first Trans Football Program. We have a lot of exciting stuff coming up! Stay tuned for more and let's rid the football ground of cis-sexist biases together.\n\nThe program is the brainchild of ScoutMe, The Keshav Suri Foundation and Bhaichung Bhutia Football Schools. Be sure to give us your support on social media \n\nBest,\nArjun Pandey\nFounder at ScoutMe", to=[str(email)])
            # emailm.send()
            # newEmail = EmailMessage('Registration - '+name, "\nEmail - "+email+"\nMobile- "+mobile +"\nMessage - " + message, to = ["arjun@scoutme.in"])
            # newEmail.send()
            # profile.save()
            email_from = settings.EMAIL_HOST_USER
            send_mail('Registration Complete!',finm, email_from,[str(email),])
            send_email('Registration - '+name, "\nEmail - "+email+"\nMobile- "+mobile +"\nMessage - " + message,email_from,["arjun@scoutme.in,"])
            return render(request, 'aftersignup.html',{"error":"Your account has been created!"})
class Contact(APIView):
    def get(self, request):
        return render(request, 'contact.html')
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        newEmail = EmailMessage('Contact Query at Kicking Gender Boundaries', "Hi "+name+"\n\nThank you for your query! We will be reaching out to you in the next 3 days.\n\nStay tuned for more! \n\nBest,\nThe Kicking Gender Boundaries Team", to = [str(email)])
        newEmail.send()
        email = EmailMessage('New Contact Query - '+subject, "Name - "+name+"\nEmail - "+email+"\nSubject - "+subject+"\nMessage - "+message, to = ["arjun@scoutme.in"])
        email.send()
        return redirect('home')
