from django.db import models

from UserLogin.models import Lab

# Create your models here.

class TestType(models.Model):
    name = models.CharField(max_length=530)
    description = models.CharField(max_length=1050)
    note = models.CharField(max_length=10000)
    interpretation = models.CharField(max_length=1110)
    
    def __str__(self):
        return self.name
    
class TestDetail(models.Model):
    testName = models.CharField(max_length=250)
    units = models.CharField(max_length=50)
    bio_ref_interval = models.CharField(max_length=50)
    testType = models.ForeignKey(TestType, on_delete=models.CASCADE)
    price = models.CharField(max_length=50)
    
    def __str__(self):
        return self.testName

class Plan(models.Model):
    name = models.CharField( max_length=350)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    test = models.ManyToManyField(TestDetail)
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name