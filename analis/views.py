from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy

from projectmanajer.models import analis_proyek,proyek,perangkat,anggota_survey,organisasi


@login_required
def dashboard(request):
    if request.session.has_key('login'):
        return render(request, 'analis/dashboard.html')
    else:
        return redirect('accounts:login')

class list_project(generic.TemplateView):
    template_name = 'analis/list-project.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs.get('pk'))
        context = super(list_project, self).get_context_data(**kwargs)
        context['proyeks'] = analis_proyek.objects.filter(analis=self.request.user)
        return context

class rekap_survey(generic.TemplateView):
    template_name ='analis/rekap-survey.html'
