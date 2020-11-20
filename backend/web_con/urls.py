from django.urls import path
from drf_spectacular import views as schema_views

from . import views

app_name = 'web_con'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.SearchView.as_view(), name='search'),
    path('call/<str:pk>', views.CallView.as_view(), name='call'),
    path('room_not_found', views.RoomNotFoundView.as_view(), name='room_not_found'),
    path('completed_call', views.CallCompoletedView.as_view(), name='completed_call'),
    path('user/<str:pk>', views.UserProfileView.as_view(), name='user_profile'),
    path('setting_recruit', views.SettingRecruitView.as_view(), name='setting_recruit'),
    # API Documentation
    path(
        'schema/',
        schema_views.SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'schema/swagger-ui/',
        schema_views.SpectacularSwaggerView.as_view(url_name='web_con:schema'),
        name='swagger-ui'
    ),
    path(
        'schema/redoc/',
        schema_views.SpectacularRedocView.as_view(url_name='web_con:schema'),
        name='redoc'
    ),
]
