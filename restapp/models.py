# Create your models here.
from django.db import models

# Create your models here.
class YoursDataModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    city = models.CharField(max_length=255)
    contract_date = models.DateField()
    created_at =models.DateField(auto_now_add=True)


class FinanceModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    city = models.CharField(max_length=255)
    contract_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)