# from django.http import request
import uuid
# import django
# from django.db import models
from django.forms.models import BaseModelForm
from django.http.response import Http404
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView
from django.db.models import Model, Q
from django.db.models.query import QuerySet
from django.core.exceptions import ValidationError
from typing import Dict, Any, Optional
from functools import reduce
from django.urls import reverse_lazy
# from out.allauth.account import forms

from util.views import ProjectBaseMixin
from accounts.models import User
from .models import Room, Tag, RoomTag
from .form import CreateRoomForm  # , CreateRoomTagForm


class IndexView(TemplateView, ProjectBaseMixin):
    template_name = 'index.html'


class RoomNotFoundView(ProjectBaseMixin, TemplateView):
    template_name = 'room_not_found.html'


class CallCompoletedView(ProjectBaseMixin, TemplateView):
    template_name = 'completed_call.html'


class SearchView(ProjectBaseMixin, ListView):
    template_name = 'search.html'
    model = Room
    queryset = Room.objects.filter(is_possible_join=True)

    def get_queryset(self) -> QuerySet[Model]:
        search_all = super().get_queryset()
        search_title = self.request.GET.get('keyword', '')
        tag_list = [key.replace('tag_', '') for key in self.request.GET.keys() if 'tag_' in key]
        self.request.session.update({
            'activate_tag_list': tag_list,
            'activate_search': search_title,
        })
        search_all = search_all.filter(
            Q(title__icontains=search_title) &
            reduce(lambda s, t: s | Q(roomtag__tag__pk=t), tag_list, Q())
        ).distinct()

        return search_all

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            'tag_list': Tag.objects.all(),
            'activate_tag_list': self.request.session['activate_tag_list'],
            'activate_search': self.request.session['activate_search']
        })
        return context_data


class CallView(ProjectBaseMixin, DetailView):
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


class UserProfileView(ProjectBaseMixin, DetailView):
    template_name = 'user_profile.html'
    model = User

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect(to='web_con:login_required')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'rooms': Room.objects.filter(roomuser__user=self.request.user),  # type: ignore
            'owner_rooms': Room.objects.filter(created_by=self.request.user),  # type: ignore
        })
        return context


class SettingRecruitView(ProjectBaseMixin, CreateView):
    template_name = 'setting_recruit.html'
    model = Room
    form_class = CreateRoomForm
    success_url = reverse_lazy('web_con:search')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tag_list': Tag.objects.all(),
        })
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        room = form.save(commit=False)
        room.id = uuid.uuid4()
        room.created_by = self.request.user
        room.is_possible_join = True
        room.save()

        tag_all = Tag.objects.all()
        for post_key in self.request.POST.keys():
            if 'tag_' in post_key:
                tag_key = post_key[4:]
                tag_instans = tag_all.get(pk=tag_key)
                roomtag = RoomTag(tag=tag_instans, room=room)
                roomtag.save()

        return super().form_valid(form)


class UpdateRoomSettingView(ProjectBaseMixin, UpdateView):
    model = Room
    template_name = 'update_room_setting.html'
    form_class = CreateRoomForm

    # def get_succss_url(self):
    #     return reverse_lazy('web_con:user/<str:pk>',kwargs = {'pk': self.kwargs['pk']})

    def get_queryset(self) -> QuerySet[Model]:
        search_all = super().get_queryset()
        search_title = self.request.GET.get('keyword', '')
        tag_list = [key.replace('tag_', '') for key in self.request.GET.keys() if 'tag_' in key]
        self.request.session.update({
            'activate_tag_list': tag_list,
            'activate_search': search_title,
        })
        search_all = search_all.filter(
            reduce(lambda s, t: s | Q(roomtag__tag__pk=t), tag_list, Q(
                title__icontains=search_title
            )),
        ).distinct()
        return search_all

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tag_list': Tag.objects.all(),
            'activate_tag_list': self.request.session['activate_tag_list'],
        })
        return context


class ParticipateRoom(ProjectBaseMixin, DetailView):
    model = Room
    template_name = 'participate_room.html'

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context.update({
    #         'activate_tag_list': self.request.session['activate_tag_list'],
    #     })
    #     return context
