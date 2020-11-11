from django.http.response import Http404
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, ListView
from django.db.models import Model
from django.db.models.query import QuerySet
from django.core.exceptions import ValidationError
from typing import Dict, Any, Optional

from util.views import DebugContextMixin
from .models import Room
from .serializers import RoomSerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})


def room_not_found(request: HttpRequest) -> HttpResponse:
    return render(request, 'room_not_found.html', {})


def completed_call(request: HttpRequest) -> HttpResponse:
    return render(request, 'completed_call.html', {})


class SearchView(DebugContextMixin, ListView):
    template_name = 'search.html'
    model = Room


class CallView(DebugContextMixin, DetailView):
    template_name = 'call.html'
    model = Room

    def get_object(self, queryset: Optional['QuerySet[Model]'] = None) -> Model:
        try:
            return super().get_object(queryset)
        except ValidationError as e:
            # UUIDがマッチしないエラーのハンドリング
            print(e)
            raise Http404('inValid UUID')

    def render_to_response(self, context: Dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        room = self.get_object()
        if isinstance(room, Room):
            if room.check_permission(self.request.user):
                return super().render_to_response(context, **response_kwargs)
            else:
                return redirect(to='web_con:index')
        else:
            raise TypeError


class RoomApiViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
