from django import forms
from django.forms import modelformset_factory
from .models import proyek, organisasi
from accounts.models import User


class proyekForm(forms.ModelForm):

    class Meta:
        model = proyek
        fields = ('nama', 'deskripsi', 'user', 'pjProyek')
        labels = {
            'nama': 'Nama Proyek',
            'deskripsi': 'Deskripsi Proyek',
            'user': "Manajer Proyek",
            'pjProyek': 'Penanggung Jawab Proyek',

        }
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama Proyek'
            }),
            'deskripsi': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Deskripsi',
                'cols ': '5',
                'rows': '5'

            }),

            'user': forms.Select(
                attrs={
                    'class': 'form-control'
                },
            ),

            'pjProyek': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama Penanggung Jawab Proyek',

            }),
        }


organisasiFormSet = modelformset_factory(
    organisasi,
    fields=('nama_organisasi',),
    extra=1,
    labels='Nama Organisasi',
    widgets={
        'nama_organisasi': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan Nama Organisasi'
        }),
    }
)

class formOrganisasi(forms.ModelForm):
    class Meta:
        model = organisasi
        fields = ('nama_organisasi', 'narasumber')
        labels = {
            'nama_organisasi': 'Nama Organisasi',
            'narasumber': 'Narasumber Organisasi',
        }
        # widgets = {
        #     'nama_organisasi': forms.TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Masukkan Nama Organisasi'
        # }),
        #     'narasumber' : forms.TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Masukkan Nama Narasumber'
        # }),
        #
        # }
