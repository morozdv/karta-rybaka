import json
from django.http.response import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Fishing


def home_page(request):
    return render(request, 'home.html')


def get_fisings(request):
    queryset = Fishing.objects.all()
    return HttpResponse(content=json.dumps([{
        'location': [o.latitude, o.longitude],
        'photos': [request.build_absolute_uri(p.path.url) for p in o.photos.all()],
        'description': o.description,
        'trophies': o.trophies,
        'boat': o.boat,
		'publication_date': o.publication_date,
		'tackle': o.tackle,
		'bait': o.bait,
		'motor': o.motor
    } for o in queryset], cls=DjangoJSONEncoder))


def save_fishing(request):
    if request.method == 'POST':
        o = Fishing.objects.create(
            latitude=request.POST.get('latitude'), 
            longitude=request.POST.get('longitude'),
            # 'photos': [request.build_absolute_uri(p.path.url) for p in o.photos.all()],
            description=request.POST.get('description'),
            trophies=request.POST.get('trophies'),
            boat=request.POST.get('boat'),
            publication_date=request.POST.get('publication_date'),
            tackle=request.POST.get('tackle'),
            bait=request.POST.get('bait'),
            motor=request.POST.get('motor'),
            user=request.user
        )

    return HttpResponse(content=json.dumps({
        'location': [o.latitude, o.longitude],
        'photos': [request.build_absolute_uri(p.path.url) for p in o.photos.all()],
        'description': o.description,
        'trophies': o.trophies,
        'boat': o.boat,
		'publication_date': o.publication_date,
		'tackle': o.tackle,
		'bait': o.bait,
		'motor': o.motor
    }, cls=DjangoJSONEncoder))