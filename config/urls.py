"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from config import local
from core.login.views import HopmeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('core.products.urls')),
    path('login/', include('core.login.urls')),
    re_path(r'^$', HopmeView.as_view(), name='home'),
]

if local.DEBUG:
    urlpatterns += static(local.STATIC_URL, document_root=local.STATIC_ROOT)
    urlpatterns += static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)
