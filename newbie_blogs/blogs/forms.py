from django.forms import ModelForm
from .models import Blogs


class BlogForm(ModelForm):
    """
     This will create the blog form using blog model.
    """
    class Meta:
        model = Blogs
        fields = ['author', 'title', 'blog_content']

