from django.contrib import admin
from .models import MyContactModel , ConnectModel

# Register your models here.

class MyContactModelAdmin(admin.ModelAdmin):
    list_display = ('use','phone','email','address')

admin.site.register(MyContactModel,MyContactModelAdmin)

class ConnectModelAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email', 'text', 'time')

admin.site.register(ConnectModel,ConnectModelAdmin)