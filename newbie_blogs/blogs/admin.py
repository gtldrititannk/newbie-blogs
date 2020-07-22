from django.contrib import admin
from .models import Blogs


# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_at', 'updated_at']
    list_filter = ['created_at',]
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Blogs,BlogsAdmin)
