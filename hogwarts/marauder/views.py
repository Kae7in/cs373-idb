from django.shortcuts import render
from django.views import generic
from marauder.models import Creature


class DetailView(generic.DetailView):
    model = Creature
    template_name = 'creatures/base.html'
