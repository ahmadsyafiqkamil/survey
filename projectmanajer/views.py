from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.http import HttpResponseRedirect
from .form import proyekForm, organisasiFormSet
from .models import organisasi, proyek


class listOrganisasiView(generic.ListView):
	model = proyek
	context_object_name = 'proyeks'
	template_name = 'pm/list_organisasi.html'
# paginate_by = 5

# class detailProyek(generic.DetailView):
# 	template_name = 'pm/detail-proyek.html'
# 	model = proyek
# 	context_object_name = 'proyek'
#
# 	def get_queryset(self):
# 		queryset = super(detailProyek, self).get_queryset()
# 		a = queryset.all().filter(pk=self.kwargs.get('pk'))
# 		print(a)
# 		return a
#
# 	def get_context_data(self, **kwargs):
# 		context = super(detailProyek, self).get_context_data()
# 		context['list_organisasi'] = organisasi.objects.all()


class detailProyek(generic.DetailView):
	model = proyek
	template_name = 'pm/detail-proyek.html'


class updateProyek(generic.edit.UpdateView):
	model = proyek


class deleteProyek(generic.edit.DeleteView):
	model = proyek


# class createProyek(generic.edit.CreateView):
# 	template_name = 'pm/proyek_form.html'
# 	model = proyek
# 	form_class = proyekForm
#
# 	def get_context_data(self, **kwargs):
# 		context = super(createProyek,self).get_context_data(**kwargs)
# 		context['formOrganisasi'] = organisasiFormSet()
# 		return context
#
#
# 	def post(self, request, *args, **kwargs):
# 		formProyek = proyekForm(request.POST)
# 		formOrganisasi = organisasiFormSet(request.POST)
# 		if formProyek.is_valid() and formOrganisasi.is_valid():
# 			proyeks = formProyek.save()
# 			for form in formOrganisasi:
# 				dataOrganisasi= form.save(commit=False)
# 				dataOrganisasi.proyek = proyeks
# 				dataOrganisasi.save()
# 				# print(dataOrganisasi)
# 			return redirect('pm:list_organisasi')
#
# 	def form_valid(self, formset):
# 		formset.save()
# 		return HttpResponseRedirect('/')
#
# 	def form_invalid(self, formset):
# 		return self.render_to_response(self.get_context_data(formset=formset))


def buatproject(request):
	if request.method == 'GET':
		formProyek = proyekForm(request.GET or None)
		formOrganisasi = organisasiFormSet(queryset=organisasi.objects.none())
	elif request.method == 'POST':
		formProyek = proyekForm(request.POST)
		formOrganisasi = organisasiFormSet(request.POST)
		if formProyek.is_valid() and formOrganisasi.is_valid():
			proyeks = formProyek.save()
			for form in formOrganisasi:
				dataOrganisasi = form.save(commit=False)
				dataOrganisasi.proyek = proyeks
				dataOrganisasi.save()
			# print(dataOrganisasi)
			return redirect('pm:list_organisasi')
	return render(request, 'pm/proyek.html', {
		'formProyek': formProyek,
		'formOrganisasi': formOrganisasi,
	})


# def detailproyek(request, pk):
# 	question = get_object_or_404(proyek, pk=pk)
# 	return render(request, 'pm/detail-proyek.html', {'proyek': question})


# @method_decorator(login_required, name='dispatch')
# class proyekView(FormView):
#     template_name = 'pm/proyek.html'
#     form_class = proyekForm
#     success_url = '/thanks/'
#
#     def form_valid(self, form):


@method_decorator(login_required, name='dispatch')
class dashboardView(generic.TemplateView):
	template_name = 'pm/dashboard.html'


@method_decorator(login_required, name='dispatch')
class perangkatView(generic.TemplateView):
	template_name = 'pm/perangkat.html'
