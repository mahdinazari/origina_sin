from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from .models import Article, Category


def make_publish(modeladmin, request, queryset):
    updated = queryset.update(status='p')

    modeladmin.message_user(request, ngettext(
    '%d story was successfully marked as published.',
    '%d stories were successfully marked as published.',
    updated,
) % updated, messages.SUCCESS)

make_publish.short_description = 'انتشار مقاله'

def make_dtaft(modeladmin, request, queryset):
    updated = queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
    '%d story was successfully marked as published.',
    '%d stories were successfully marked as published.',
    updated,
) % updated, messages.SUCCESS)

make_dtaft.short_description = 'پیش نویس کردن مقاله'


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'publish',
        'categories_list',
        'get_thumbnail'
    )
    list_filter = ('status', 'publish')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at', 'publish']

    actions = [make_publish, make_dtaft]

    def categories_list(self, object):
        categories = ", ".join([c.title for c in object.category.all()])
        return categories

    categories_list.short_description = 'دسته بندی'


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('title', 'status', 'position', 'parent')
    list_filter = ('status', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1

