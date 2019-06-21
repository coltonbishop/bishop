from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import os
# Create your views here.

def landing(request):
	context = {
	}
	return render(request, 'landing/index.html', context)

def resume(request):
	objectpath = 'projects/static/resume.pdf'
	return serve(request, os.path.basename(objectpath), os.path.dirname(objectpath))