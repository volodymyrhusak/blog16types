from django.conf.urls import url
from .views import homePage

urlpatterns = [
    url(r'^$', homePage, name='homePage'),
]