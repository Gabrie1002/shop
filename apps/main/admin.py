from django.contrib import admin
from .models import Page, PageInLine


class PageItemInLine(admin.TabularInline):
    model = PageInLine
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [PageItemInLine, ]
    list_display = ['title', 'slug']