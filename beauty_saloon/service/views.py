from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from service.models import *


class MainListView(ListView):

    template_name = 'service/index.html'

def index(request):
    return render(request, 'service/index.html')


class ProductList(ListView):
    model = Product
    slug_field = 'url'
    context_object_name = 'products'

    def get_queryset(self):
        subsub_id = self.kwargs['subsub_id']
        queryset = super().get_queryset()
        return queryset.filter(subsub_id=subsub_id)



