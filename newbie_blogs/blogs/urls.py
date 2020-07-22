from django.urls import path

from .views import CreateBlogView

urlpatterns = [
     path('create/', CreateBlogView.as_view(), name='create_blog'),
]


