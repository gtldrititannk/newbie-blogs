from django.views.generic import TemplateView, View, DetailView, ListView
from django.shortcuts import render, redirect

# app imports
from .forms import BlogForm


class CreateBlogView(View):
    """
     This will create the new blog.
    """
    http_method_names = ['get', 'post']
    template_name = "create_blog.html"

    def get(self, request):
        form = BlogForm(initial={'author': request.user})
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        This method checks the form contents and saves blogs details.
        """
        form = BlogForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, self.template_name, context)
