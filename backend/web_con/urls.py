from django.urls import path
from django.conf import settings

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
    path('update_room_setting/<str:pk>', views.UpdateRoomSettingView.as_view(), name='update_room_setting'),
    path('participate_room/<str:pk>', views.ParticipateRoom.as_view(), name='participate_room'),
]

if settings.DEBUG:
    from drf_spectacular import views as schema_views

    urlpatterns = urlpatterns + [
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
