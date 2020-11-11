from rest_framework import routers

from . import views

app_name = 'web_con_api'

urlpatterns = []

router = routers.DefaultRouter()
router.register('rooms', views.RoomApiViewSet)
urlpatterns += router.urls
