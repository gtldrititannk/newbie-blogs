from django.apps import apps
from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = 'index.html'
    paginate_by = 3

    def get(self, request):
        blog_model = apps.get_model('blogs', 'Blogs')  # Importing Blog model of blogs app.
        blog_obj = blog_model.objects.all()  # Retrieving blogs from database.
        context = {'blog_obj': blog_obj}
        return render(request, self.template_name, context)

