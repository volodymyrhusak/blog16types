import logging
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth, TruncYear
from django.views.decorators.csrf import csrf_protect
from .models import PostModel, PostCommentModel
from .form import PostCommentModelForm


# Create your views here.

def blog(request):
    postsArchive = PostModel.objects.all() \
                       .annotate(month=TruncMonth('createTime'), year=TruncYear('createTime')) \
                       .values('year', 'month') \
                       .annotate(sumViews=Sum('views')) \
                       .values('year', 'month', 'sumViews') \
                       .order_by('-sumViews')[:6]

    page = request.GET.get('page')
    month = request.GET.get('month')
    year = request.GET.get('year')
    find = request.GET.get('find')
    if month and year:
        postsAll = PostModel.objects.filter(createTime__month=month, createTime__year=year) \
            .annotate(Count('postcommentmodel')) \
            .order_by('-createTime')
    elif find:
        postsAll = PostModel.objects \
            .annotate(Count('postcommentmodel')) \
            .order_by('-createTime')
    else:
        postsAll = PostModel.objects \
            .annotate(Count('postcommentmodel')) \
            .order_by('-createTime')

    paginator = Paginator(postsAll, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts,
               'MY_DATE_FORMAT': settings.MY_DATE_FORMAT,
               'postsArchive': postsArchive}
    context.update(tabpanelView())

    return render(request, 'blog.html', context)


@csrf_protect
def getPost(request, postName):
    context = {}
    page = request.GET.get('page')
    post = PostModel.objects.get(title=postName)

    if not request.session.get('view', None):
        request.session['view'] = []

    if not postName in request.session['view']:
        request.session['view'].append(postName)
        request.session.save()
        post.views += 1
        post.save()


    postsArchive = PostModel.objects.all() \
                       .annotate(month=TruncMonth('createTime'), year=TruncYear('createTime')) \
                       .values('year', 'month') \
                       .annotate(sumViews=Sum('views')) \
                       .values('year', 'month', 'sumViews') \
                       .order_by('-sumViews')[:6]

    if request.POST:
        form = PostCommentModelForm(request.POST)
        if form.is_valid():
            saveForm = form.save(commit=False)
            saveForm.post = post
            saveForm.save()
        else:
            context.update({'formErrors':form})
    

    commentsAll = PostCommentModel.objects.filter(post=post).order_by('-createTime')
    paginator = Paginator(commentsAll, 3)
    countComments = len(commentsAll)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    

            # print(form.errors)

    context.update({'post': post,
               'comments': comments,
               'countComments': countComments,
               'MY_DATE_FORMAT': settings.MY_DATE_FORMAT,
               'postsArchive': postsArchive
               })
    context.update(tabpanelView())
    return render(request, 'post.html', context)


def selectLog():
    l = logging.getLogger('django.db.backends')
    l.setLevel(logging.DEBUG)
    l.addHandler(logging.StreamHandler())


def tabpanelView():
    popularPosts = PostModel.objects.order_by('-views', '-likes')[:5]
    lastPosts = PostModel.objects.order_by('-createTime')[:5]
    lastComments = PostCommentModel.objects.order_by('-createTime')[:5]
    return {'popularPosts': popularPosts,
            'lastPosts': lastPosts,
            'lastComments': lastComments}


def addComments(post=None):
    # m = PostModel.objects.all().delete()
    # m = PostCommentModel.objects.all().delete()
    # for i in range(1, 29):
    #     m = PostModel()
    #     m.title = 'Post{}'.format(i)*5
    #     m.body = 'Post{} '.format(i) * 250
    #     m.image = 'images/800px500.png'
    #     m.save()

    post = PostModel.objects.all()
    for p in post:
        for i in range(1, 29):
            m = PostCommentModel()
            m.userName = 'user{}'.format(i)
            m.userEmail = 'user{0}@user{0}.user{0}'.format(i)
            m.body = 'user{} '.format(i) * 50
            m.post = p
            m.save()
