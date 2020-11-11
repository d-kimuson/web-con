from django.views.generic.base import TemplateResponseMixin, ContextMixin
from pprint import pprint
from typing import Any, Dict

from django.conf import settings


class ProjectBaseMixin(TemplateResponseMixin, ContextMixin):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context.update({
            'user': user,
        })

        if settings.DEBUG:
            print('=== context ===')
            pprint(context)

        return context
