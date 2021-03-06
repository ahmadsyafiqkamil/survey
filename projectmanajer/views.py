from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy

from .form import proyekForm, organisasiFormSet, formPerangkat, formMember, formPlotSurveyor,organisasiForm
from .models import organisasi, proyek, perangkat, anggota_survey,analis_proyek
from accounts.models import User

@method_decorator(login_required, name='dispatch')
class listProyek(generic.ListView):
    model = proyek
    context_object_name = 'proyeks'
    template_name = 'pm/list_proyek.html'


@method_decorator(login_required, name='dispatch')
class detailorganisasi(generic.edit.UpdateView):
    model = organisasi
    fields = ['nama_organisasi', 'narasumber']
    template_name = 'pm/detail-organisasi.html'

    def form_valid(self, form):
        post = form.save()
        return redirect('pm:list_proyek')


@method_decorator(login_required, name='dispatch')
class updateProyek(generic.edit.UpdateView):
    model = proyek
    fields = ['nama', 'deskripsi', 'user', 'pjProyek']
    template_name = 'pm/update-proyek.html'

    def form_valid(self, form):
        post = form.save()
        return redirect('pm:list_proyek')


class deleteProyek(generic.edit.DeleteView):
    model = proyek
    template_name = 'pm/delete.html'
    success_url = reverse_lazy('pm:list_proyek')


@login_required
def buatproject(request):
    if request.method == 'GET':
        formProyek = proyekForm(request.GET or None)
        formOrganisasi = organisasiFormSet(queryset=organisasi.objects.none())
    elif request.method == 'POST':
        formProyek = proyekForm(request.POST)
        formOrganisasi = organisasiFormSet(request.POST)
        if formProyek.is_valid() and formOrganisasi.is_valid():
            # proyek.user = User.id
            proyeks = formProyek.save()

            # proyek.save(update_fields=['user'])
            for form in formOrganisasi:
                dataOrganisasi = form.save(commit=False)
                dataOrganisasi.proyek = proyeks
                dataOrganisasi.save()
            return redirect('pm:list_proyek')
        else:
            pass

    return render(request, 'pm/proyek.html', {
        'formProyek': formProyek,
        'formOrganisasi': formOrganisasi,
    })


class tambahOrganisasi(generic.edit.CreateView):
    model = organisasi
    # fields = ['nama_organisasi','narasumber','proyek']
    form_class = organisasiForm
    template_name = 'pm/tambah-organisasi.html'
    success_url = reverse_lazy('pm:list_proyek')

    def get_form_kwargs(self):
        print(self.kwargs.get('pk'))
        kw = super(tambahOrganisasi, self).get_form_kwargs()
        kw['id_proyek'] = self.kwargs.get('pk')
        return kw

@method_decorator(login_required, name='dispatch')
class updateProyek(generic.edit.UpdateView):
    model = proyek
    fields = ['nama', 'deskripsi', 'user', 'pjProyek']
    template_name = 'pm/update-proyek.html'

    def form_valid(self, form):
        post = form.save()
        return redirect('pm:list_proyek')


@method_decorator(login_required, name='dispatch')
class dashboardView(generic.TemplateView):
    template_name = 'pm/dashboard.html'


@method_decorator(login_required, name='dispatch')
class perangkatView(generic.TemplateView):
    template_name = 'pm/perangkat.html'


@method_decorator(login_required, name='dispatch')
class detailProyek(generic.TemplateView):
    template_name = 'pm/detail-proyek.html'

    def get_context_data(self, *args, **kwargs):
        context = super(detailProyek, self).get_context_data(*args, **kwargs)
        context['proyek'] = get_object_or_404(proyek, pk=self.kwargs.get('pk'))
        context['organisasi'] = organisasi.objects.filter(proyek=self.kwargs.get('pk'))
        return context


class lihat_perangkat(generic.TemplateView):
    template_name = 'pm/lihat-perangkat.html'

    def get_context_data(self, *args, **kwargs):
        context = super(lihat_perangkat, self).get_context_data(*args, **kwargs)
        try:
            context['perangkat'] = perangkat.objects.get(proyek_id=self.kwargs.get('pk'))
        except perangkat.DoesNotExist:
            context['perangkat'] = None
        return context


class deleteOrganisasi(generic.DeleteView):
    model = organisasi
    template_name = 'pm/delete.html'
    success_url = reverse_lazy('pm:list_proyek')


class hapus_perangkat(generic.edit.DeleteView):
    model = perangkat
    template_name = 'pm/delete.html'
    success_url = reverse_lazy('pm:list_proyek')


class buat_perangkat(generic.edit.CreateView):
    model = perangkat
    # fields = ['proyek','perangkat']
    form_class = formPerangkat
    template_name = 'pm/buat-perangkat.html'
    success_url = reverse_lazy('pm:perangkat')


class update_perangkat(generic.edit.UpdateView):
    model = perangkat
    # fields = ['proyek','perangkat']
    form_class = formPerangkat
    template_name = 'pm/update-perangkat.html'

    def form_valid(self, form):
        form.save()
        return redirect('pm:list_proyek')


class manajemen_member(generic.ListView):
    model = User
    template_name = 'pm/manajemen-member.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data_user'] = User.objects.exclude(staff=True)
        return context


class detail_member(generic.edit.UpdateView):
    model = User
    form_class = formMember
    template_name = 'pm/detail-member.html'
    success_url = reverse_lazy('pm:manajemen_member')


class hapus_member(generic.edit.DeleteView):
    model = User
    template_name = 'pm/delete.html'
    success_url = reverse_lazy('pm:manajemen_member')


class plot_surveyor(generic.edit.CreateView):
    model = anggota_survey
    # fields = ['survey_organisasi','anggota']
    form_class = formPlotSurveyor
    template_name = 'pm/plot-surveyor.html'
    success_url = reverse_lazy('pm:list_proyek')

    def get_form_kwargs(self):
        kw = super(plot_surveyor, self).get_form_kwargs()
        kw['id_organisasi'] = self.kwargs.get('pk')
        return kw


class detail_organisasi_surveyor(generic.TemplateView):
    # model = anggota_survey
    template_name = 'pm/detail-organisasi-surveyor.html'

    def get_context_data(self, *args, **kwargs):
        context = super(detail_organisasi_surveyor, self).get_context_data(*args, **kwargs)
        context['surveyor'] = anggota_survey.objects.filter(survey_organisasi=self.kwargs.get('pk'))
        # context['surveyor'] = anggota_survey.objects.values_list('anggota__user_name',flat= True).filter(survey_organisasi=self.kwargs.get('pk'))
        return context


class hapus_organisasi_surveyor(generic.edit.DeleteView):
    model = anggota_survey
    template_name = 'pm/delete.html'
    success_url = reverse_lazy('pm:list_proyek')

class plot_analis(generic.edit.CreateView):
    template_name = 'pm/plot-analis.html'
    model = analis_proyek
    fields = ['proyek','analis']
    success_url = reverse_lazy('pm:list_proyek')

class detail_analis_surveyor(generic.TemplateView):
    template_name = 'pm/detail-analis-survey.html'

    def get_context_data(self, **kwargs):
        context = super(detail_analis_surveyor, self).get_context_data(**kwargs)
        try:
            context['analis'] = analis_proyek.objects.filter(proyek_id=self.kwargs.get('pk'))
        except perangkat.DoesNotExist:
            context['analis'] = None
        return context

class delete_analis_surveyor(generic.edit.DeleteView):
    model = analis_proyek
    success_url = reverse_lazy('pm:list_proyek')
    template_name = 'pm/delete.html'