from django.contrib import admin

from Reports.models import *

# Register your models here.
class Patientadmin(admin.ModelAdmin):
    list_display=['result','test','dateTimeCollection','dateTimeReceived','dateTimeReported']

# class Onetimeadmin(admin.ModelAdmin):
#     list_display = ['',]

admin.site.register(PatientTestDetail,Patientadmin)
admin.site.register(OneTimeTest)
