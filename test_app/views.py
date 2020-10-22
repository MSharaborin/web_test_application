from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView, DeleteView
from django.views.generic.list import ListView
from .models import Signalling
from .forms import AddSignalling


class Siren(ListView):
    model = Signalling
    paginate_by = 10
    template_name = 'index.html'
    context_object_name = 'signalling'


class CreateSiren(CreateView):
    model = Signalling
    template_name = 'create_page.html'
    form_class = AddSignalling


class UpdateSiren(UpdateView):
    model = Signalling
    template_name = 'update_page.html'
    form_class = AddSignalling


class DetailSiren(DetailView):
    model = Signalling
    template_name = 'detail_page.html'


class DeleteSiren(DeleteView):
    model = Signalling
    template_name = 'delete_page.html'
    success_url = reverse_lazy('index_url')
