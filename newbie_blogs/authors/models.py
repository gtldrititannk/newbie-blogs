from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    """
    This stores all the details regarding authors.
    """
    birth_date = models.DateTimeField(null=True, blank=True, verbose_name='author_birth_date')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='author_address')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
