from django.contrib import admin

from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_filter = ('title', )


targets = (
    (Room, RoomAdmin),
)

for target in targets:
    admin.site.register(target[0], target[1])
