from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

from .forms import UserLoginForm, UserRegisterForm
# Create your views here.


def login_view(request):
	print(request.user.is_authenticated())
	# next = request.Get.get('next')
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		Username = form.cleaned_data.get("username")
		Password = form.cleaned_data.get("password")
		user = authenticate(username= username, password = password)
		login(request, user)
		# if next:
			# return redirect(next)
		return redirect ("/")
	return render(request, 'form.html', {"form":form, "title": title})

def register_view(request):
	title = "Register"

	form = UserRegisterForm(request.POST or None)
	# next = request.Get.get('next')
	if form.is_valid():
		user = form.save(commit= False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username= user.username, password = password)

		login(request, user)
		# if next:
			# return redirect(next)
		return redirect ("/")


	context = {
			"form": form,
			"title": title
	}
	return render(request, 'acc.html', context)



def logout_view(request):
	title = "Logout"

	logout(request)
	return redirect ("/")

	# return render(request, 'form.html', {})