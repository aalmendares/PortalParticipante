from rest_framework.routers import DefaultRouter
from posts.api.views import solicitud_separacionesListView

router_post = DefaultRouter()
router_post.register(prefix='separaciones', basename='separaciones', viewset=solicitud_separacionesListView)