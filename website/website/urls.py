from website.settings import dev
from django.contrib import admin
from django.urls import path, include
from base.views import page_not_found
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('captcha/', include('captcha.urls')),
                  path('__debug__/', include('debug_toolbar.urls'))
              ] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')), path('', include('base.urls')),
    path('users/', include('users.urls', namespace='users')), prefix_default_language=False
)

if dev.DEBUG:
    urlpatterns += static(dev.MEDIA_URL, document_root=dev.MEDIA_ROOT)

handler404 = page_not_found

admin.site.site_header = _('Admin panel')
admin.site.index_title = _('Space website')
