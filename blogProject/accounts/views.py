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
	# loginform = UserLoginForm(request.POST or None)
	form = UserLoginForm(request.POST or None)

	# if loginform.is_valid():
	if form.is_valid():
		Username = form.cleaned_data.get("username")
		Password = form.cleaned_data.get("password")
		user = authenticate(username= Username, password = Password)
		login(request, user)
		# if next:
			# return redirect(next)
		return redirect ("/blog/")


	# def get_context_data(self, **kwargs):
	# 	context = super(login_view, self).get_context_data(**kwargs)
	# 	# context['inform'] = UserLoginForm()
	# 	context['inform'] = UserLoginForm.fields.all()
	# 	return context

	# return render(request, 'accin.html', {"form":loginform, "title": title})
	return render(request, 'accin.html', {"form":form, "title": title})


def register_view(request):
	title = "Register"

	# regform = UserRegisterForm(request.POST or None)
	form = UserRegisterForm(request.POST or None)

	# next = request.Get.get('next')
	# if regform.is_valid():
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
		# return redirect ("/")



	context = {
			# "form": regform,
			"form": form,
			"title": title
	}
	return render(request, 'acc.html', context)



def logout_view(request):
	title = "Logout"

	logout(request)
	return redirect ("/")


def actions_view(request):
	title = "Logout"

	logout(request)
	return render(request, 'actions.html', {})

	# return redirect ("/")

	# return render(request, 'form.html', {})