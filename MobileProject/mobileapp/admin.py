from django.contrib import admin
from mobileapp.models import mobile_model

# Register your models here.


class mobile_modelAdmin(admin.ModelAdmin):
    search_fields = ['Model','JAN_Code']




admin.site.register(mobile_model,mobile_modelAdmin)
