from django.db import models

# Create your models here.

class News(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField(max_length=500)
    Author = models.CharField(max_length=50)
