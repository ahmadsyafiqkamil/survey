import stat

from django import forms
from .models import survey
from projectmanajer.models import organisasi
from projectmanajer.models import anggota_survey
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
from .models import lampiran


class surveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = ['hasil_survey', 'anggota_survey']

    def __init__(self, *args, **kwargs):
        super(surveyForm, self).__init__(*args, **kwargs)
        self.fields['anggota_survey'].queryset = anggota_survey.objects.exclude(status=1)

class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)



# class uploadForm(forms.ModelForm):
#     class Meta:
#         model = lampiran
#         fields = ['file']
#         widgets = {
#             'file': forms.TextInput(attrs={
#                 'class': 'file-uploader',
#             }),
#         }
