from django.apps import apps
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializer

blog_model = apps.get_model('blogs', 'Blogs')  # Importing Blog Model.


class BlogsView(viewsets.ModelViewSet):
    """
      It allows Authenticated user for CRUD operations.
    """
    permission_classes = [IsAuthenticated]  # Authenticate the user through token.
    queryset = blog_model.objects.all()
    serializer_class = BlogSerializer
