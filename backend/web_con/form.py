# from django.db import models
# from django.db.models.fields import DateTimeField
# from django.forms import fields
# from django.forms import widgets
from django.forms.widgets import DateTimeInput
from .models import Room, Tag
from django import forms
import datetime
# from django.contrib.admin.widgets import AdminDateWidget


class CreateRoomForm(forms.ModelForm):
    dt_now = datetime.datetime.now()
    td = datetime.timedelta(hours=1)
    dt_one_hour_after = dt_now + td
    start_datetime = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': dt_now.strftime('%Y-%m-%d %H:%M:%S')
    }))
    end_datetime = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': dt_one_hour_after.strftime('%Y-%m-%d %H:%M:%S')
    }))

    class Meta:
        model = Room
        fields = ('title', 'description', 'start_datetime', 'end_datetime',)
        widgets = {
            'start_datetime': DateTimeInput(format='%m/%d/%y %H:%M:%S'),
            'end_datetime': DateTimeInput(format='%m/%d/%y %H:%M:%S'),
        }