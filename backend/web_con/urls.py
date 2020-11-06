from django.urls import path

from . import views

app_name = 'web_con'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.SearchView.as_view(), name='search'),
    path('call/<str:pk>', views.CallView.as_view(), name='call'),
    path('room_not_found', views.room_not_found, name='room_not_found'),
    path('completed_call', views.completed_call, name='completed_call'),
]
