"""newbie_blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import path,re_path,include
from rest_framework.authtoken.views import obtain_auth_token


from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blogs/', include('blogs.urls')),
    path('', IndexView.as_view(), name='index'),
    path('create-token/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('blogs-api/',include('blogs_api.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]

admin.site.site_header = 'NewBie Blogs Admin'
admin.site.site_title = 'NewBie Blogs'
admin.site.index_title = "Welcome to the NewBie Blogs."
