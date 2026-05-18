from django.contrib import admin
from django.utils.html import format_html
from .models import Photo, Tag, Like


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin for Tag model."""

    list_display = ['name']
    search_fields = ['name']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Admin for Photo model with thumbnail preview."""

    list_display = ['title', 'uploaded_by', 'created_at', 'thumbnail']
    list_filter = ['tags', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = ['tags']

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px; height:40px; object-fit:cover; border-radius:4px;" />',
                obj.image.url
            )
        return '—'
    thumbnail.short_description = 'Preview'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """Admin for Like model."""

    list_display = ['user', 'photo', 'value']
    list_filter = ['value']