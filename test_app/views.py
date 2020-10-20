from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from .models import Signalling


class Siren(ListView):
    """
    TODO доработать
    """
    model = Signalling
    paginate_by = 10
    template_name = 'index.html'
    context_object_name = 'siren'