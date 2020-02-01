from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.

# def signup(request):
# 	if request.method == "POST":
# 		signup_form = UserCreationForm(request.POST)
# 		if signup_form.is_valid():
# 			signup_form.save()
# 		return redirect('/')
# 	else: #HTTP method 가 GET인 경우
# 		signup_form = UserCreationForm()

# 	return render(request, 'signup.html', {'signup_form':signup_form})
def signup(request):
	if request.method == "POST":
		if request.POST["password1"]==request.POST["password2"]:
			user = User.objects.create_user(
				username=request.POST["username"], password=request.POST["password1"])
			auth.login(request, user)
			return redirect('/')
		return render(request, 'signup.html')
	return render(request, 'signup.html')

# def login(request):
# 	if request.method == "POST":
# 		login_form = AuthenticationForm(request, request.POST)
# 		if login_form.is_valid():
# 			auth_login(request, login_form.get_user())
# 		return redirect('/')
# 	else:
# 		login_form = AuthenticationForm()
# 	return render(request, 'login.html',{'login_form':login_form})
def login(request):
	if request.method =="POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = auth.authenticate(request, username = username, password = password)
		if user is not None:
			auth_login(request, user)
			return redirect("/")
		else:
			return render(request, 'login.html',
				{'error': 'usernameor password is incorrect'})
	else:
		return render(request, 'login.html')


def logout(request):
	auth_logout(request)
	return redirect('/')