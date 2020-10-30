from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.base import ContextMixin
from django.db.models import Model
from django.db.models.query import QuerySet
from django.core.exceptions import ValidationError
from pprint import pprint
from typing import Dict, Any, Optional

from django.conf import settings
from .models import Room


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})


def room_not_found(request: HttpRequest) -> HttpResponse:
    return render(request, 'room_not_found.html', {})


class DebugContextMixin(ContextMixin):
    # 後で Util 系の置き場を作って移動する
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        if settings.DEBUG:
            pprint(context_data)
        return context_data


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
