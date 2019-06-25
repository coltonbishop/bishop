from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import os

# Create your views here.

def language(request):
	context = {
	}
	return render(request, 'gallery/index.html', context)

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
	context = {
	}
	return render(request, 'gallery/symcnn.html', context)

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