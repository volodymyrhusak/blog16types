from django.shortcuts import render
from blog.models import PostModel
from django.db.models import Count
from django.conf import settings

# Create your views here.

def homePage(request):
    # posts = PostModel.objects.order_by('-createTime')[:6]
    posts = PostModel.objects.annotate(Count('postcommentmodel')).order_by('-createTime')[:6]
    context = {'MY_DATE_FORMAT': settings.MY_DATE_FORMAT,
    		'posts':posts}
    return render(request, 'homePage.html', context)
