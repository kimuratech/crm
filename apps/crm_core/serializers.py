from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'industry']


from .models import Lead, Deal, Task


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'account', 'name', 'email', 'status']


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['id', 'account', 'title', 'value', 'stage']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'account', 'subject', 'due_date', 'completed']
