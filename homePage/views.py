from django.shortcuts import render
from blog.models import PostModel
from django.db.models import Count

# Create your views here.

def homePage(request):
    # posts = PostModel.objects.order_by('-createTime')[:6]
    posts = PostModel.objects.annotate(Count('postcommentmodel')).order_by('-createTime')[:6]
    context = {'posts':posts}
    return render(request, 'homePage.html', context)
