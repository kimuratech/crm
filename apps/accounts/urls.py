from django.urls import path, include
from rest_framework import routers
from .api import ContactViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('api/', include(router.urls)),
    path('contacts/', views.contact_list, name='contact-list'),
]
