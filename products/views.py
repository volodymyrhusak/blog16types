from django.shortcuts import render
from .models import (AdviceModel,
                     AdviceCategoryModel,
                     CourseModel,
                     OnCourseModel)
from django.conf import settings

# Create your views here.

def advice(request):
    categories = AdviceCategoryModel.objects.filter(use=True)
    advices = AdviceModel.objects.filter(category__in=categories)
    context = {'advices':advices,
               'categories':categories}
    return render(request, 'advice.html', context)

def courses(request):
    courses = CourseModel.objects.filter(use=True)
    onCourses = OnCourseModel.objects.filter(category__in=courses)
    context = {'courses': courses,
               'onCourses': onCourses}
    return render(request, 'courses.html',context)

def cooperation(request):
    context = {
        'EMAIL_HOST_USER':settings.EMAIL_HOST_USER
    }
    return render(request, 'cooperation.html',context)