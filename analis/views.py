from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    if request.session.has_key('login'):
        return render(request, 'analis/dashboard.html')
    else:
        return redirect('accounts:login')

