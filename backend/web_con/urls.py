from django.urls import path

from . import views

app_name = 'web_con'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.SearchView.as_view(), name='search'),
    path('call/<str:pk>', views.CallView.as_view(), name='call'),
    path('room_not_found', views.RoomNotFoundView.as_view(), name='room_not_found'),
    path('completed_call', views.CallCompoletedView.as_view(), name='completed_call'),
    path('user/<str:pk>', views.UserProfileView.as_view(), name='user_profile')
]
