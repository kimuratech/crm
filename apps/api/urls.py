from rest_framework import routers
from django.urls import path, include
from apps.crm_core.api import AccountViewSet, LeadViewSet, DealViewSet, TaskViewSet
from apps.accounts.api import ContactViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'deals', DealViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
