from django.contrib import admin

from .models import Article


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish')
    list_filter = ('status', 'publish')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at', 'publish']

