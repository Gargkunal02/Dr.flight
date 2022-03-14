from django.contrib import admin

from TestDetails.models import *

# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display=['name','price','description']
    
class TestTypeAdmin(admin.ModelAdmin):
    list_display=['name','description','note','interpretation']
    
class TestDetailsAdmin(admin.ModelAdmin):
    list_display=['testName','units','bio_ref_interval','testType','price']
    
admin.site.register(TestDetail,TestDetailsAdmin)
admin.site.register(TestType,TestTypeAdmin)
admin.site.register(Plan,PlanAdmin)