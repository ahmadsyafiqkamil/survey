from django import forms
from .models import survey
from projectmanajer.models import anggota_survey

class surveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = ['hasil_survey']

        widgets = {
            'hasil_survey': forms.HiddenInput(attrs={
                'id':'hasil_survey'
            })
        }

