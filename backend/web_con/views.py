from django.http import request
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.utils.timezone import activate
from django.views.generic import DetailView, ListView
from django.db.models import Model, Q
from django.db.models.query import QuerySet
from django.core.exceptions import ValidationError
from typing import Dict, Any, Optional
from functools import reduce

from util.views import DebugContextMixin
from .models import Room, Tag


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})


def room_not_found(request: HttpRequest) -> HttpResponse:
    return render(request, 'room_not_found.html', {})


def completed_call(request: HttpRequest) -> HttpResponse:
    return render(request, 'completed_call.html', {})


class SearchView(DebugContextMixin, ListView):
    template_name = 'search.html'
    model = Room
    queryset = Room.objects.filter(is_possible_join=True)

    def get_queryset(self) -> QuerySet[Model]:
        search_all = super().get_queryset()
        search_title = self.request.GET.get('keyword','')
        tag_list = [key.replace('tag_', '') for key in self.request.GET.keys() if 'tag_' in key]
        self.request.session.update({
            'activate_tag_list': tag_list,
            'activate_search':search_title,
        })
        search_all = search_all.filter(
            reduce(lambda s, t: s | Q(roomtag__tag__pk=t), tag_list, Q(title__icontains=search_title)),
        ).distinct()
        return search_all

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'tag_list': Tag.objects.all(),
            'activate_tag_list':self.request.session['activate_tag_list'],
            'activate_search':self.request.session['activate_search']
        })
        return context_data


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
