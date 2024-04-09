from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class Content(models.Model):
    header = models.CharField(max_length=255, verbose_name=_('Header'))
    post = models.TextField(blank=True, verbose_name=_('Content'))
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name=_('Slug'))
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name=_('Photo')
    )
    author = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, related_name='content', null=True, default=None,
        verbose_name=_('Author')
    )
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, related_name='content', null=True, verbose_name=_('Categories')
    )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation time'))
    time_update = models.DateTimeField(auto_now=True, verbose_name=_('Time of change'))
    is_published = models.BooleanField(default=True, verbose_name=_('Status'))

    objects = models.Manager()
    published = PublishManager()

    class Meta:
        verbose_name = _('object')
        verbose_name_plural = _('Objects')

    def get_absolute_url(self):
        return reverse('content', kwargs={'slug': self.slug})


class Category(models.Model):
    cat_name = models.CharField(max_length=100, db_index=True, verbose_name=_('Category'))
    cat_slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.cat_slug})
