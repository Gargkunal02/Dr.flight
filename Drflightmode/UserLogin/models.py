from platform import mac_ver
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_lab = models.BooleanField(default=False)


class Lab(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=50)
    lab_no = models.CharField(max_length=30,default='1221')
    # patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    # doctor = models.ManyToManyField(Doctor)
    # plan = models.ManyToManyField(Plan)
    
    def __str__(self):
        return self.user.first_name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    phonenumber = models.CharField(max_length=10)
    secondaryPhoneNumber = models.CharField(max_length=10)
    email= models.CharField(max_length=250)
    address = models.TextField()
    photo = models.ImageField(upload_to="patient", height_field=None, width_field=None, max_length=None)
    gender = models.CharField(max_length=50)
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    phonenumber = models.CharField(max_length=10)
    secondaryPhoneNumber = models.CharField(max_length=10)
    email= models.CharField(max_length=250)
    address = models.TextField()
    photo = models.ImageField(upload_to='doctor', height_field=None, width_field=None, max_length=None)
    gender = models.CharField(max_length=50)
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE)
    hospital = models.CharField(max_length=300)
    years_of_experience = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.user.first_name