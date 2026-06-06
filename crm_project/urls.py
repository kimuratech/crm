from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
import os


class SpaIndexView(TemplateView):
    template_name = 'index.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SpaIndexView.as_view(), name='home'),
    path('', include('apps.accounts.urls')),
    path('', include('apps.crm_core.urls')),
    path('api/', include('apps.api.urls')),
]


# Development-only: serve legacy /assets/* URLs from static/assets to avoid 404s
if settings.DEBUG:
    from django.views.static import serve

    assets_root = os.path.join(settings.BASE_DIR, 'static', 'assets')

    urlpatterns += [
        re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': assets_root}),
    ]
