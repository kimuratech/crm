from rest_framework import viewsets
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def list(self, request, *args, **kwargs):
        """Return a plain list of accounts (not the paginated envelope) to
        match test expectations and simplify API consumption for the SPA.
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Additional viewsets for CRM core models
from rest_framework import filters
from .models import Lead, Deal, Task
from .serializers import LeadSerializer, DealSerializer, TaskSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'status']


class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'stage']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['subject']
