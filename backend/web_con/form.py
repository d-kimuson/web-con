# from django.db import models
# from django.db.models.fields import DateTimeField
# from django.forms import fields
# from django.forms import widgets
from .models import Room
from django import forms
from datetime import datetime, timedelta
# from django.contrib.admin.widgets import AdminDateWidget
from typing import Optional, Any


def convert_datetime_to_html_attrs(dt: Optional[datetime]) -> Optional[str]:
    """datetimeによる日付・時刻をhtmlで使う文字列に変換

    Args:
        dt (Optional[datetime]): 対象の時間

    Returns:
        Optional[str]: 変換された文字列
    """
    return dt.strftime("%Y-%m-%dT%H:%M") if isinstance(dt, datetime) else None


def get_calender_datetime_widget(
    min: Optional[datetime] = None,
    max: Optional[datetime] = None,
    step_minute: int = 1,
) -> forms.DateTimeInput:
    """カレンダー型の日付&時間入力ウィジェットを作成する関数

    秒数の入力には対応しません

    Args:
        min (Optional[datetime], optional): 最小の入力値. Defaults to None.
        max (Optional[datetime], optional): 最大の入力値. Defaults to None.
        step_minute (int, optional): 入力の刻み値(単位: 分). Defaults to 1

    Returns:
        forms.DateTimeInput: 作成されたウィジェット
    """
    form = forms.DateTimeInput(
        attrs={
            "type": "datetime-local",
            "min": convert_datetime_to_html_attrs(min),
            "max": convert_datetime_to_html_attrs(max),
            "step": 60 * step_minute,
        },
        format="%Y-%m-%dT%H:%M"
    )

    return form


class CreateRoomForm(forms.ModelForm):
    dt_now = datetime.now()
    td = timedelta(hours=1)
    dt_one_hour_after = dt_now + td

    args = {
        "year": dt_now.year,
        "month": dt_now.month,
        "day": dt_now.day,
    }

    # 削除予定: DateTimeField に変更
    # start_datetime = forms.SplitDateTimeField()
    # end_datetime = forms.SplitDateTimeField()
    start_datetime = forms.DateTimeField(
        widget=get_calender_datetime_widget(
            min=dt_now,
            max=dt_now + timedelta(days=14),
            step_minute=30
        )
    )
    end_datetime = forms.DateTimeField(
        widget=get_calender_datetime_widget(
            min=dt_now,
            max=dt_now + timedelta(days=14),
            step_minute=30
        )
    )

    class Meta:
        model = Room
        fields = ('title', 'description', 'start_datetime', 'end_datetime',)
        now = datetime.now()
        # 削除予定: フィールド定義に移動済み
        # widgets = {
        # 'start_datetime': DateTimeInput(format='%m/%d/%y %H:%M:%S'),
        # 'end_datetime': DateTimeInput(format='%m/%d/%y %H:%M:%S'),
        # }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        now = datetime.now()
        if kwargs.get("instance", None) is None:
            # デフォルト値を
            kwargs.update({
                "initial": {
                    "start_datetime": convert_datetime_to_html_attrs(datetime(
                        year=now.year,
                        month=now.month,
                        day=now.day,
                        hour=now.hour + 1
                    )),
                    "end_datetime": convert_datetime_to_html_attrs(datetime(
                        year=now.year,
                        month=now.month,
                        day=now.day,
                        hour=now.hour + 2
                    ))
                }
            })

        super().__init__(*args, **kwargs)
