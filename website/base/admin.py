from .models import Content, Category
from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('header',)}
    list_display = ('id', 'header', 'category', 'time_create', 'is_published')
    list_display_links = ('id', 'header')
    ordering = ['header', 'time_create']
    list_editable = ['category', 'is_published']
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['header', 'category__cat_name']
    list_filter = ['category__cat_name', 'is_published']

    @admin.action(description=_('Publish selected entries'))
    def set_published(self, request, queryset):
        counter = queryset.update(is_published=Content.Status.PUBLISHED)
        self.message_user(request, f'{counter} entries modified')  # !

    @admin.action(description=_('Unpublish selected records'))
    def set_draft(self, request, queryset):
        counter = queryset.update(is_published=Content.Status.DRAFT)
        self.message_user(request, f'{counter} entries withdrawn from publication', messages.WARNING)  # !


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name')
    list_display_links = ('id', 'cat_name')
