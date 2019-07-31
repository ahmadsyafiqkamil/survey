import stat

from django import forms
from .models import survey
from projectmanajer.models import organisasi
from projectmanajer.models import anggota_survey

class surveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = ['hasil_survey','anggota_survey']

    def __init__(self,*args, **kwargs):
        super(surveyForm, self).__init__(*args, **kwargs)
        self.fields['anggota_survey'].queryset = anggota_survey.objects.exclude(status=1)
