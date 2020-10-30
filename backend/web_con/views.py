from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})


class CallView(TemplateView):
    template_name = 'call.html'
