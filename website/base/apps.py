from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    verbose_name = _("Site Objects")
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
