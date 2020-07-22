from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render, redirect

# app imports
from .models import Blogs
from .forms import BlogForm


class CreateBlogView(TemplateView):
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


class BlogDetailsView(DetailView):
    http_method_names = ['get']
    template_name = "blog_detail.html"

    def get(self, request, pk=None):
        if pk:
            blog = Blogs.objects.get(pk=pk)
            context = {
                'blog': blog
            }
        else:
            context = {
                'message': 'Invalid Input',
            }

        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        return render(request, self.template_name)


class BlogEditView(UpdateView):
    http_method_names = ['get', 'post']
    template_name = 'edit_blog.html'

    def get(self, request, pk=None):
        blog = Blogs.objects.get(pk=pk)
        fields_dict = {
            'author': blog.author,
            'title': blog.title,
            'blog_content': blog.blog_content,
        }
        form = BlogForm(initial=fields_dict)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        blog_obj = Blogs.objects.get(pk=pk)
        form = BlogForm(request.POST, instance=blog_obj)

        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            context = {
                'form': form,
                'message': 'Blog Details Update Failed Because of Invalid Data.',
                'danger': True
            }

        return render(request, self.template_name, context)


class BlogDeleteView(DeleteView):
    http_method_names = ['get', 'post']
    template_name = 'delete_blog.html'

    def get(self, request, pk=None):
        blog = Blogs.objects.get(pk=pk)
        context = {'blog': blog}
        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        blog = Blogs.objects.get(pk=pk)
        form = BlogForm(request.POST, instance=blog)
        blog.delete()
        context = {
            'message': 'Blog Deleted Successfully',
            'danger': False
        }
        return render(request, self.template_name, context)
