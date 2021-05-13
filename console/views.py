from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from console.forms import SignUpForm
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
	# import pdb;pdb.set_trace()
	return render(request,'console/apphome.html')


def signupview(request):
	if request.method == 'POST':
		# import pdb;pdb.set_trace()
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			# import pdb;pdb.set_trace()
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.profile.merrital_status = form.cleaned_data.get('merrital_status')
			user.save()
			messages.success(request,'successfully registered')
			return redirect(reverse('console:home'))
	else:
		form = SignUpForm()
	return render(request,'console/signup.html', {'form':form})



def validate_username(request):
	# import pdb;pdb.set_trace()
	username = request.GET.get('username', None)

	data = {
	'is_taken':User.objects.filter(username__iexact=username).exists()
	}
	return JsonResponse(data)



def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			messages.success(request,'successfully logged in')
			return redirect(reverse('console:home'))
		else:
			messages.error(request,'crdential not matched ')
			form = AuthenticationForm()
			return render(request,'console/login.html',{'form':form} )

	else:
		form = AuthenticationForm()
	return render(request,'console/login.html', {'form':form})


def signout(request):
	logout(request)
	return redirect(reverse('console:login'))



# class SignUpView(CreateView):
# 	template_name = "console/signup.html"
# 	form_class = UserCreationForm