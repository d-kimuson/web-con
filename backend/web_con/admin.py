from django.contrib import admin

from .models import Room, RoomTag, Tag, RoomUser


class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'start_datetime', 'end_datetime', 'is_possible_join')
    list_filter = ('title', 'start_datetime', 'end_datetime', 'is_possible_join')


targets = (
    (Room, RoomAdmin),
    (RoomTag, None),
    (Tag, None),
    (RoomUser, None)
)

for target in targets:
    admin.site.register(target[0], target[1])
