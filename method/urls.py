from django.conf.urls import url
from .views import method

urlpatterns = [
    url(r'^', method, name='method'),
]