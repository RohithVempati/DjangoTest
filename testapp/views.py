from django.shortcuts import render
from django.http import *

# Create your views here.

def testapp(request):
    return HttpResponse("Hello world!!")
