from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from projectmanajer.models import anggota_survey
from accounts.models import User

# Create your views here.
@login_required
def dashboard(request):
    if request.session.has_key('login'):
        return render(request, 'surveyor/home.html')
    else:
        return redirect('login')


class list_project(generic.TemplateView):
    template_name = 'surveyor/list-project.html'

    def get_context_data(self, **kwargs):
        context = super(list_project, self).get_context_data(**kwargs)
        context['list_project'] = anggota_survey.objects.filter(anggota=self.request.user)
        return context

class survey_organisasi(generic.TemplateView):
    template_name = 'surveyor/survey-organisasi.html'






