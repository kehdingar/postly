from django.contrib import admin

from django.contrib import admin
from .models import Vote

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'value']
    list_filter = ['post']
    search_fields = ['user__username', 'post__title']

