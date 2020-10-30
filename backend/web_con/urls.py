from django.urls import path

from . import views

app_name = 'web_con'

urlpatterns = [
    path('', views.index, name='index'),
    path('call/<str:pk>', views.CallView.as_view(), name='call'),
]
