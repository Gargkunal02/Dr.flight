from cgi import test
from django.db import models

from TestDetails.models import *
from UserLogin.models import *
# Create your models here.


class PatientTestDetail(models.Model):
    patient = models.ManyToManyField(Patient)
    result = models.CharField(max_length=50)
    test = models.ForeignKey(TestDetail, on_delete=models.CASCADE)
    dateTimeCollection = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateTimeReceived = models.DateTimeField(auto_now=True, auto_now_add=False)
    dateTimeReported = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    # def __str__(self):
    #     return self.patient
    
class OneTimeTest(models.Model):
    TestInput = models.ManyToManyField(PatientTestDetail)
    
    # def __str__(self):
    #     return self.TestInput