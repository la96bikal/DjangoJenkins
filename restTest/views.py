from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request, id):
	a = id
	b = ''
	for x in range(0, a+1):
		b = b + str(x) +  "Hello world <br>"
	return HttpResponse(b)