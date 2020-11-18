from rest_framework import routers

from . import viewsets

app_name = 'web_con_api'

urlpatterns = []

router = routers.DefaultRouter()
router.register('rooms', viewsets.RoomViewSet)
urlpatterns += router.urls
