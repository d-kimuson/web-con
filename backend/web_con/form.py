# from django.db import models
# from django.db.models.fields import DateTimeField
# from django.forms import fields
# from django.forms import widgets
from django.forms.widgets import DateTimeInput
from .models import Room
from django import forms
# from django.contrib.admin.widgets import AdminDateWidget


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('title', 'description', 'start_datetime', 'end_datetime')
        widgets = {
            'start_datetime': DateTimeInput(format='%m/%d/%y %H:%M:%S'),
            # 'start_datetime': AdminDateWidget(),
            'end_datetime': DateTimeInput(format='%m/%d/%y %H:%M:%S'),
        }
