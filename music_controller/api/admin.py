from django.contrib import admin

from .models import Room

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    fields = ['code', 'host', 'guest_can_pause', 'votes_to_skip']

admin.site.register(Room, RoomAdmin)
