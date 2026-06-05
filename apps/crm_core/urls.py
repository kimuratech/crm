from django.urls import path, include
from rest_framework import routers
from .api import AccountViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = [
    path('api/', include(router.urls)),
    path('accounts/', views.account_list, name='account-list'),
    path('accounts/create/', views.account_create, name='account-create'),
    path('accounts/<int:pk>/', views.account_detail, name='account-detail'),
]
