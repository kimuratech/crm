from django.urls import path, include
from rest_framework import routers
from .api import ContactViewSet
from . import views
from .views_auth import RegisterView, MeView

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/me/', MeView.as_view(), name='me'),
    path('contacts/', views.contact_list, name='contact-list'),
]
