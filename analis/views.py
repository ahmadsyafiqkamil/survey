from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy

from projectmanajer.models import analis_proyek,proyek,perangkat,anggota_survey,organisasi
from surveyor.models import survey

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


class list_organisasi(generic.TemplateView):
    template_name = 'analis/list-organisasi.html'

    def get_context_data(self, **kwargs):
        context = super(list_organisasi, self).get_context_data(**kwargs)
        context['organisasi'] = anggota_survey.objects.select_related().filter(survey_organisasi__proyek_id=self.kwargs.get('pk_proyek'))
        return context

class hasil_survey(generic.TemplateView):
    template_name = 'analis/hasil-survey.html'

    def get_context_data(self, **kwargs):
        context = super(hasil_survey, self).get_context_data(**kwargs)
        context['data'] = survey.objects.get(anggota_survey=self.kwargs.get('pk_anggota_survey'))
        return context

class rekap_survey(generic.TemplateView):
    template_name ='analis/rekap-survey.html'
