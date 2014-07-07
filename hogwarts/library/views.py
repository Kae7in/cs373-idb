from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. AVADA KEDAVRA!")

#Potions
def potions(request):
	potions = Potion.objects.order_by('name')
	template = loader.get_template('potions/index.html')
	context = RequestContext(request, {
		'potions': potions,
	})
	return HttpResponse(template.render(context))

def potion(request, potion_id):
	raise Http404

def brew(request, potion_id):
	raise Http404

#Characters
def characters(request):
	raise Http404

def character(request, character_id):
	raise Http404

#Spells
def spells(request):
	raise Http404

def spell(request, spell_id):
	raise Http404
