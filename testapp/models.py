from django.db import models

# Create your models here.
#test

class News(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField(max_length=1000)
    Author = models.CharField(max_length=50)
