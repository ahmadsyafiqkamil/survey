from django import forms
from django.forms import modelformset_factory
from .models import proyek, organisasi, perangkat
import json
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

    def __init__(self, *args, **kwargs):
        super(proyekForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(staff= True)


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


class formPerangkat(forms.ModelForm):
    class Meta:
        model = perangkat
        fields = ['nama_perangkat','proyek', 'perangkat']

        widgets = {
            'perangkat' : forms.Textarea(attrs={
                'placeholder': 'Masukkan hasil dari tab JsonEditor',

            }),
            'nama_perangkat':forms.TextInput(attrs={
                'placeholder': 'Masukkan Nama Perangkat',
            })
        }

    def __init__(self, *args, **kwargs):
        super(formPerangkat, self).__init__(*args, **kwargs)
        self.fields['proyek'].queryset = proyek.objects.exclude(id__in=perangkat.objects.values("proyek_id"))

class formMember(forms.ModelForm):
    class Meta :
        model = User
        fields =['user_name','email','active','staff','surveyor','analis']

    labels = {
        'user_name': 'Nama Anggota',
        'email': 'Alamat Email',
        'active': "Status Aktif",
        'staff': 'Status Project Manajer',
        'surveyor': 'Status Surveyor',
        'analis': 'Status Analis',

    }


