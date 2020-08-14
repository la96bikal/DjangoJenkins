from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Hey just a comment
#another comment for test

def hello(request, id):
	a = id
	b = ''
	for x in range(0, a+1):
		b = b + str(x) +  "Hello world and the demo to the world<br> Checking CD 1 2 3<br> "
	return HttpResponse(b)