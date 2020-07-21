from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import Author


class CustomAuthorAdmin(UserAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 'birth_date', 'username', 'email',
    ]

    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name', 'last_name', 'email',
                'address','birth_date',
            )
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),

    )


# admin.site.register(User, UserAdmin)
admin.site.register(Author, CustomAuthorAdmin)
