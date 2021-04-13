from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import smtplib
#Function to send emails
def bill(usermail,msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('example@gmail.com', 'password')
        smtp.sendmail('example@gmail.com', usermail, msg)

# Create your views here.

def index(request):
	API_KEY="YOUR_API_KEY"
	if request.method == 'POST':
		email=request.POST['email'],
		name=request.POST['name'],
		amount=request.POST['amount']
		msg= f'Thank you {name}, for your donation of ${amount}'
		#bill(email, msg) #to be used with authentic email credentials
	return render(request, 'index.html', {'API_KEY':API_KEY})


