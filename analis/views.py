import nltk
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
        return render(request, '../templates/analis/dashboard.html')
    else:
        return redirect('accounts:login')

class list_project(generic.TemplateView):
    template_name = '../templates/analis/list-project.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs.get('pk'))
        context = super(list_project, self).get_context_data(**kwargs)
        context['proyeks'] = analis_proyek.objects.filter(analis=self.request.user)
        return context


class list_organisasi(generic.TemplateView):
    template_name = '../templates/analis/list-organisasi.html'

    def get_context_data(self, **kwargs):
        context = super(list_organisasi, self).get_context_data(**kwargs)
        context['organisasi'] = anggota_survey.objects.select_related().filter(survey_organisasi__proyek_id=self.kwargs.get('pk_proyek'))
        return context

class hasil_survey(generic.TemplateView):
    template_name = '../templates/analis/hasil-survey.html'

    def get_context_data(self, **kwargs):
        context = super(hasil_survey, self).get_context_data(**kwargs)
        context['data'] = survey.objects.get(anggota_survey=self.kwargs.get('pk_anggota_survey'))
        return context

class rekap_survey(generic.TemplateView):
    template_name = '../templates/analis/rekap-survey.html'

    def get_context_data(self, **kwargs):
        context = super(rekap_survey, self).get_context_data(**kwargs)
        # context['data'] = survey.objects.select_related().filter(anggota_survey__survey_organisasi__proyek_id=self.kwargs.get('pk_proyek'))
        data = survey.objects.select_related().values_list("hasil_survey").filter(anggota_survey__survey_organisasi__proyek_id=self.kwargs.get('pk_proyek'))
        data_survey = []
        data_survey.clear()
        for x in data:
            data_survey.append(x.hasil_survey)
            
        jumlah_organisasi = len(data)
        kunci = data_survey[1].keys()
        
        
        return context

