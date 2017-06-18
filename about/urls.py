from django.conf.urls import url
from .views import aboutMe, aboutUse , aboutProjects , aboutBooks, aboutResponse

urlpatterns = [
    url(r'^about_me/$', aboutMe, name='aboutMe'),
    url(r'^about_use/$', aboutUse, name='aboutUse'),
    url(r'^about_books/$', aboutBooks, name='aboutBooks'),
    url(r'^about_projects/$', aboutProjects, name='aboutProjects'),
    url(r'^about_response/$', aboutResponse, name='aboutResponse'),
]