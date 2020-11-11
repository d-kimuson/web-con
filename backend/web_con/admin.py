from django.contrib import admin

from .models import Room,RoomTag,Tag


class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
    list_filter = ('title', )


targets = (
    (Room, RoomAdmin),
    (RoomTag, None),
    (Tag, None),
)

for target in targets:
    admin.site.register(target[0], target[1])
