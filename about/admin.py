# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (IUseModel,
                     IUseCategoryModel,
                     ApplicationProjectModel,
                     BooksModel,
                     AboutMeModel,
                     ProjectModel)

# Register your models here.
class ApplicationProjectAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName','time' ,'areaCode','telNum','emailId')

admin.site.register(ApplicationProjectModel,ApplicationProjectAdmin)

class BooksModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'bookName','time')

admin.site.register(BooksModel,BooksModelAdmin)

class AboutMeModelAdmin(admin.ModelAdmin):
    list_display = ('slogan', 'use','text','time')

admin.site.register(AboutMeModel,AboutMeModelAdmin)


class IUseCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('use', 'name')

admin.site.register(IUseCategoryModel,IUseCategoryModelAdmin)

class IUseModelAdmin(admin.ModelAdmin):
    list_display = ('use', 'name', 'descr', 'link','category')

admin.site.register(IUseModel,IUseModelAdmin)

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('use', 'text')

admin.site.register(ProjectModel,ProjectModelAdmin)