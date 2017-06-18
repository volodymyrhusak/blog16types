from django.contrib import admin
from .models import MethodInUseModel

# Register your models here.

class MethodInUseModelAdmin(admin.ModelAdmin):
    list_display = ('text','use','parent')

admin.site.register(MethodInUseModel,MethodInUseModelAdmin)