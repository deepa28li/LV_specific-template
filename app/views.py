from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from app.models import *

class school_list(ListView):
    model=School
    context_object_name="schools"

class school_detail(DetailView):
    model=School
    context_object_name='sclobject'

class create_school(CreateView):
    model=School
    fields='__all__'

class School_update(UpdateView):
    model=School
    fields='__all__'
