from rest_framework import serializers
from app_service.models import Service


class ServiceSerializers(serializers.Serializer):
    
    class Meta:
        model = Service
        fields = '__all__'
        

class GetServiceSerializers(serializers.Serializer):
    
    
    class Meta:
        model = Service
        fields = ['id', 'service_price', ' service_type', 'owner_id']