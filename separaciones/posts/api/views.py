from rest_framework.viewsets import ModelViewSet
from posts.models import solicitud_separaciones
from posts.api.serializers import solicitud_separacionesSerializer

class solicitud_separacionesListView(ModelViewSet):
    serializer_class=solicitud_separacionesSerializer
    queryset=solicitud_separaciones.objects.all()