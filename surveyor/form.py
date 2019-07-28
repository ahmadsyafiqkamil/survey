from django import forms
from .models import survey
from projectmanajer.models import organisasi
from projectmanajer.models import anggota_survey

class surveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = ['hasil_survey','anggota_survey']

        # def __init__(self,*args, **kwargs):
        #     id_anggota_survey = kwargs.pop('id_anggota_survey')
        #     super(surveyForm, self).__init__(*args, **kwargs)
        #     self.fields['anggota_survey'].queryset = organisasi.objects.filter(anggota_survey =id_anggota_survey )

        # labels = {
        #     'hasil_survey': 'Hasil Survey',
        #
        # }
        # widgets = {
        #     'hasil_survey': forms.Textarea(attrs={
        #         'id':'id_hasil_survey',
        #         'placeholder': 'Masukkan Nama Proyek',
        #         'class': 'form-control',
        #
        #     }),
        #     'anggota_survey':forms.HiddenInput(
        #         attrs={
        #             'id': 'id_anggota_survey',
        #         }
        #     )
        # }
