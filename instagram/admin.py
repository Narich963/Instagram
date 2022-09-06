from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('get_photo', 'author', 'publish_date', 'comment', 'like_count')
    list_filter = ('author', 'publish_date', 'like_count', 'comment')
    search_fields = ('author',)
    raw_id_fields = ('author',)
    date_hierarchy = 'publish_date'
    ordering = ('publish_date', 'author')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=100">')
        else:
            return 'No photo'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_avatar', 'name', 'followers', 'followed')
    list_filter = ('name', 'followers', 'followed')
    search_fields = ('name', 'followers', 'followed')

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width=100>')
        else:
            return 'No avatar'




