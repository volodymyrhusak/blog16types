from django.conf.urls import url
from .views import blog , getPost

urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^(?P<postName>.*)/$', getPost, name='post'),
]

