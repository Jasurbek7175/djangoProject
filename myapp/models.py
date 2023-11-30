from django.db import models

# Create your models here.
class YourDataModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class DataModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    city = models.CharField(max_length=255)