from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing(request):
	context = {
	}
	return render(request, 'landing/index.html', context)