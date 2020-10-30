from django.views.generic.base import ContextMixin
from pprint import pprint
from typing import Any, Dict

from django.conf import settings


class DebugContextMixin(ContextMixin):
    # 後で Util 系の置き場を作って移動する
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        if settings.DEBUG:
            pprint(context_data)
        return context_data
