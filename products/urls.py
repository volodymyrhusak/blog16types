from django.conf.urls import url
from .views import advice, courses, cooperation

urlpatterns = [
    url(r'^advice/$', advice, name='advice'),
    url(r'^courses/$', courses, name='courses'),
    url(r'^cooperation/$', cooperation, name='cooperation'),
]