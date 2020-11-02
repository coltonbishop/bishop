from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import os

# Create your views here.

def language(request):
	context = {
	}
	return render(request, 'landing/index.html', context)

def wengga(request):
	context = {
	}
	return render(request, 'gallery/wengga.html', context)

def deepmesh(request):
	context = {
	}
	return render(request, 'gallery/deepmesh.html', context)

def alquilando(request):
	context = {
	}
	return render(request, 'gallery/alquilando.html', context)

def hive(request):
	context = {
	}
	return render(request, 'gallery/hive.html', context)

def rype(request):
	context = {
	}
	return render(request, 'gallery/rype.html', context)

def symcnn(request):
	objectpath = 'projects/static/assistedmodeling.pdf'
	return serve(request, os.path.basename(objectpath), os.path.dirname(objectpath))

def wengganet(request):
	context = {
	}
	return render(request, 'gallery/wengganet.html', context)

def donatello(request):
	context = {
	}
	return render(request, 'gallery/donatello.html', context)

def personal(request):
	context = {
	}
	return render(request, 'gallery/personal.html', context)

def esg(request):
	context = {
	}
	return render(request, 'gallery/esg.html', context)

def tigertales(request):
	context = {
	}
	return render(request, 'gallery/tigertales.html', context)

def puentes(request):
	context = {
	}
	return render(request, 'gallery/puentes.html', context)

def activelearning(request):
	objectpath = 'projects/static/activelearning.pdf'
	return serve(request, os.path.basename(objectpath), os.path.dirname(objectpath))

def nmt(request):
	objectpath = 'projects/static/nmt.pdf'
	return serve(request, os.path.basename(objectpath), os.path.dirname(objectpath))

def pokedex(request):
	objectpath = 'projects/static/pokedex.pdf'
	return serve(request, os.path.basename(objectpath), os.path.dirname(objectpath))

def dnc_pipeline(request):
	objectpath = 'projects/static/dnc_pipeline.pdf'
	return serve(request, os.path.basename(objectpath), os.path.dirname(objectpath))
