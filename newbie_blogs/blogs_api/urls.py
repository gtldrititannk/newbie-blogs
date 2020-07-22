from django.urls import path,include
from rest_framework import routers
from .views import BlogsView


router = routers.DefaultRouter()
router.register('', BlogsView)


urlpatterns = [
    path('v1/', include(router.urls)),
]