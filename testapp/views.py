from django.shortcuts import render
from django.http import *
from rest_framework.decorators import api_view
from .models import News

# Create your views here.

def testapp(request):
    return HttpResponse("Hello world!!")

@api_view(["POST"])
def testAppPost(request):
    payload = request.data
    news = News.objects.create(**payload)
    data = News.objects.filter(pk=news.pk).values().first()
    response = {"code":200, "data": data}
    return JsonResponse(response)

@api_view(["GET"])
def fetchNews(request,id=0):
    data = News.objects.values().all()
    data = list(data)
    if(id):
        data = News.objects.filter(id=int(id)).values().first()
        return JsonResponse({"code":200,"data":data})
    #print(data)
    return JsonResponse({"code":200,"data":data})
