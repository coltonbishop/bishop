from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import os

# Create your views here.

def language(request):
	context = {
	}
	return render(request, 'gallery/index.html', context)