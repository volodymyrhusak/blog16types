from django.contrib import admin
from .models import (AdviceCategoryModel,
                     AdviceModel,
                     CourseModel,
                     OnCourseModel)


# Register your models here.
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('use', 'name', 'descr', 'descrBelow', 'link')


admin.site.register(CourseModel, CourseModelAdmin)


class OnCourseModelAdmin(admin.ModelAdmin):
    list_display = ('use', 'text', 'category')


admin.site.register(OnCourseModel, OnCourseModelAdmin)


class AdviceModelAdmin(admin.ModelAdmin):
    list_display = ('use', 'text', 'category')


admin.site.register(AdviceModel, AdviceModelAdmin)


class AdviceCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('use', 'name')


admin.site.register(AdviceCategoryModel, AdviceCategoryModelAdmin)
