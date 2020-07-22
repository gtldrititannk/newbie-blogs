from django.urls import path

from .views import CreateBlogView, BlogEditView, BlogDeleteView,BlogDetailsView

urlpatterns = [
     path('create/', CreateBlogView.as_view(), name='create_blog'),
     path('detail/<int:pk>/', BlogDetailsView.as_view(), name='blog_detail'),
     path('update/<int:pk>/', BlogEditView.as_view(), name='edit_blog'),
     path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),

]


