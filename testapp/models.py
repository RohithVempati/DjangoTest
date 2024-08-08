from django.db import models

# Create your models here.
#test

class News(models.Model):
    Title = models.CharField(max_length=200)
    Content = models.TextField(max_length=500)
    Author = models.CharField(max_length=50)
