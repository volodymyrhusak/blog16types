from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import MethodInUseModel

# Create your views here.

def method(request):
    inUseParent = MethodInUseModel.objects.exclude(parent__isnull=False)
    inUseChild = MethodInUseModel.objects.exclude(parent__isnull=True)
    context = {
        'inUseParent':inUseParent,
        'inUseChild':inUseChild,
    }
    return render(request, 'method.html',context)