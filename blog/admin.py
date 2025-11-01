from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "heading",
        "created_at",
        "publication_at",
    )
    list_filter = (
        "publication_at",
        "created_at",
    )
    search_fields = (
        "heading",
        "content",
    )
