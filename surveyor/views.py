from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from projectmanajer.models import anggota_survey, perangkat,proyek
from .form import surveyForm
from accounts.models import User
from .models import survey
from django.urls import reverse_lazy


@login_required
def dashboard(request):
    if request.session.has_key('login'):
        return render(request, 'surveyor/home.html')
    else:
        return redirect('login')


class list_project(generic.TemplateView):
    template_name = 'surveyor/list-project.html'

    def get_context_data(self, **kwargs):
        print(self.request.user)
        context = super(list_project, self).get_context_data(**kwargs)
        context['list_project'] = anggota_survey.objects.filter(anggota=self.request.user)
        return context


class survey_organisasi(generic.edit.CreateView):
    template_name = 'surveyor/survey-organisasi.html'
    model = survey
    fields = ['hasil_survey']
    success_url = reverse_lazy("surveyor:list_project")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.anggota_survey_id = anggota_survey.objects.get(anggota_id=self.request.user.pk).pk
        self.object.save()
        # anggota_survey.objects.filter(pk=).update(status = 1)
        return super().form_valid((form))

    def get_context_data(self, *args, **kwargs):
        print(self.request.user.pk)
        context = super(survey_organisasi, self).get_context_data(*args, **kwargs)
        try:
            context['perangkat'] = perangkat.objects.get(proyek_id=self.kwargs.get('pk'))
            context['survey'] = survey.objects.filter()
        except perangkat.DoesNotExist:
            context['perangkat'] = None
        return context


class rekap_survey(generic.TemplateView):
    template_name = 'surveyor/rekap-surveyor.html'


class edit_survey(generic.edit.UpdateView):
    template_name = 'surveyor/edit-survey.html'
    model = survey
    fields = ['hasil_survey']
