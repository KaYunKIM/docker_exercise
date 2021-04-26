from rest_framework import serializers
from .models import Visits

class VisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = ['visitor_name', 'visit_datetime']

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = ['visitor_name']