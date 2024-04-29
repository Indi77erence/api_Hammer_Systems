import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response

from ..models import User, VerificationCode
import time


# import random
# import string
# from twilio.rest import Client


@csrf_exempt
def login_view(request):
	return render(request, 'login.html')


@csrf_exempt
def create_user(request):
	if request.method == 'POST':
		phone_number = request.POST.get('phone_number')
		correct_number = '+' + ''.join(filter(str.isdigit, phone_number))
		user, created = User.objects.get_or_create(phone_number=correct_number)

		if created:
			user.generate_invite_code()
			code_for_login = send_code_for_login(correct_number)
			VerificationCode.objects.create(verif_code=code_for_login, user=user, created=datetime.datetime.now())
			request.session['verification_code'] = code_for_login
			request.session['phone_number'] = correct_number
			return redirect('auth_user')

		return redirect('auth_user')
	return render(request, 'enter_verification_code.html')


@csrf_exempt
def auth_user(request):
	if request.method == 'POST':
		entered_code = request.POST.get('verification_code')
		phone_number = request.session.get('phone_number')
		user = User.objects.get(phone_number=phone_number)
		verification_code = VerificationCode.objects.filter(user=user).last()
		if str(verification_code) == entered_code:
			return redirect('user', pk=user.pk)
		else:
			return Response(status=status.HTTP_401_UNAUTHORIZED)
	return render(request, 'enter_verification_code.html')


def send_code_for_login(receiver):
	time.sleep(2)
	# code = random.randint(1000, 9999)
	# client = Client(username=TWILIO_SID, password=TWILIO_TOKEN)
	# client.messages.create(body=code, from_=NUMBER, to=receiver)
	# return str(code)
	return "1111"
