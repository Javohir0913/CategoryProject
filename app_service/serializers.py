from rest_framework import serializers
from app_service.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
 

class GetServiceSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Service
        fields = ['id', 'service_name', 'service_type',]