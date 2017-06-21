"""type16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.conf import settings
from django.contrib import admin

def handler404(request):
    response = render(RequestContext(request), '404.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, '404.html')
    response.status_code = 500
    return response

urlpatterns = [
    # url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    # url(r'^500/$', TemplateView.as_view(template_name='404.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('homePage.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^method/', include('method.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^media/', include('imagefit.urls')),
    url(r'^', handler404),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

