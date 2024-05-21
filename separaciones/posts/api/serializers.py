from rest_framework import serializers
from posts.models import solicitud_separaciones

class solicitud_separacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = solicitud_separaciones
        fields = '__all__'