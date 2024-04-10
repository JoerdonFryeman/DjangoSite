from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UploadFiles(models.Model):
    file = models.FileField(upload_to='upload_files')


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True, verbose_name=_('Photo'))
    first_name = models.TextField(blank=True, null=True, verbose_name=_('Name'))
    last_name = models.TextField(blank=True, null=True, verbose_name=_('Surname'))
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name=_('Date of birth'))
