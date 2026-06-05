from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def root_redirect(request):
    return redirect('account-list')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_redirect, name='home'),
    path('', include('apps.accounts.urls')),
    path('', include('apps.crm_core.urls')),
    path('api/', include('apps.api.urls')),
]
