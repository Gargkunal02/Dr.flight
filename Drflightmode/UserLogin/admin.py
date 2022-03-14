from django.contrib import admin

from UserLogin.models import *

# Register your models here.

class Labadmin(admin.ModelAdmin):
    list_display=['user','location']

class DoctorAdmin(admin.ModelAdmin):
    list_display=['user']
    
class PatientAdmin(admin.ModelAdmin):
    list_display=['user','age','gender','phonenumber','email','address']
    
admin.site.register(User)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Lab,Labadmin)