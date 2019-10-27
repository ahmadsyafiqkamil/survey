from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import User


# Create your views here.

def login(request):
	if request.method == 'POST':
		
		user = auth.authenticate(email=request.POST['email'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			request.session['login'] = user.get_full_name()
			if user.is_staff:
				return redirect('pm:dashboard')
			elif user.is_analis:
				return redirect("analis:dashboard")
			elif user.is_surveyor:
				return redirect("surveyor:dashboard")
			else:
				raise Http404("Halaman yang anda cari tidak ada")
		else:
			return render(request, '../templates/account/login.html', {'error': 'Cek Username dan Password anda'})
	else:
		return render(request, '../templates/account/login.html')


def register(request):
	if request.method == 'POST':
		if request.POST['ps1'] == request.POST['ps2']:
			try:
				user = User.objects.get(email=request.POST['email'])
				return render(request, '../templates/account/register.html', {'error': 'nama sudah terpakai'})
			except User.DoesNotExist:
				user = User.objects.create_user(email=request.POST['email'],user_name=request.POST['username'], password=request.POST['ps1'])
				auth.login(request, user)
				return redirect('accounts:login')
		else:
			return render(request, '../templates/account/register.html', {'errorps': 'password tidak sama'})
	else:
		return render(request, '../templates/account/register.html')


def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('accounts:login')
