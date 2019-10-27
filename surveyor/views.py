from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from projectmanajer.models import anggota_survey, perangkat, proyek
from .form import surveyForm,UploadForm
from accounts.models import User
from .models import survey, lampiran
from django.urls import reverse_lazy


@login_required
def dashboard(request):
    if request.session.has_key('login'):
        return render(request, '../templates/surveyor/home.html')
    else:
        return redirect('login')


class list_project(generic.TemplateView):
    template_name = '../templates/surveyor/list-project.html'

    def get_context_data(self, **kwargs):
        print(self.request.user.pk)
        context = super(list_project, self).get_context_data(**kwargs)
        context['hasil_survey'] = survey.objects.filter(anggota_survey__anggota_id=self.request.user,
                                                        anggota_survey__status=1).select_related()
        context['list_project_belum_survey'] = anggota_survey.objects.filter(anggota_id=self.request.user, status=0)
        return context


class survey_organisasi(generic.edit.CreateView):
    template_name = '../templates/surveyor/survey-organisasi.html'
    model = survey
    form_class = surveyForm
    success_url = reverse_lazy("surveyor:list_project")

    def form_valid(self, form):
        form.save()
        anggota_survey_id = survey.objects.latest('anggota_survey_id').get_anggota_survey()
        print(anggota_survey_id)
        anggota_survey.objects.filter(id=anggota_survey_id).update(status=1)
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        print(self.request.user.pk)
        context = super(survey_organisasi, self).get_context_data(*args, **kwargs)
        context['uploadForm'] = UploadForm
        try:
            context['perangkat'] = perangkat.objects.get(proyek_id=self.kwargs.get('pk'))
            context['survey'] = survey.objects.filter()

        except perangkat.DoesNotExist:
            context['perangkat'] = None
        return context

class uploadLampiran(generic.edit.CreateView):
    model = lampiran

class rekap_survey(generic.TemplateView):
    template_name = '../templates/surveyor/rekap-surveyor.html'


class edit_survey(generic.edit.UpdateView):
    template_name = '../templates/surveyor/edit-survey.html'
    # form_class = UploadForm
    model = survey
    fields = ['hasil_survey']

    def get_context_data(self, **kwargs):
        print(self.kwargs.get('pk'))
        context = super(edit_survey, self).get_context_data(**kwargs)
        context['data'] = survey.objects.get(id=self.kwargs.get('pk'))
        context['uploadForm'] = UploadForm
        return context

class tes(generic.TemplateView):
    template_name = '../templates/surveyor/edit-survey.html'


