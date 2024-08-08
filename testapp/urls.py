from django.urls import path
from . import views

urlpatterns = [
    path('testapps/',views.testapp,name='testapp'),
    path('testapi/',views.testAppPost),
    path('getnews/<str:id>',views.fetchNews),
    path('getnews/',views.fetchNews)
]