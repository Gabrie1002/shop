from django.contrib import admin
from .models import Page, PageInLine
from tinymce.widgets import AdminTinyMCE
from django.db.models.fields import TextField


class PageItemInLine(admin.TabularInline):
    model = PageInLine
    extra = 0
    formfield_overrides = {
        TextField: {'widget': AdminTinyMCE(attrs={'cols': 80, 'rows': 40},)}
    }


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [PageItemInLine, ]
    list_display = ['title', 'slug']