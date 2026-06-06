from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


class SpaIndexView(TemplateView):
    template_name = 'index.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SpaIndexView.as_view(), name='home'),
    path('', include('apps.accounts.urls')),
    path('', include('apps.crm_core.urls')),
    path('api/', include('apps.api.urls')),
]
