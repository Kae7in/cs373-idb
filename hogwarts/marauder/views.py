from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def creature_detail(request, topic, creature_id):
    return render(request, '{0}/{1}.html'.format(topic, creature_id))
