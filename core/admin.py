from django.contrib import admin
from .models import Post, Comment, SocialModel




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_posted", "is_published", "view_count")
    list_filter = ("date_posted", "is_published", "author")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "date_posted"
    ordering = ("-date_posted",)
    fieldsets = (
        (None, {"fields": ("title", "slug", "content", "image", "view_count")}),
        (
            "Advanced Options",
            {
                "classes": ("collapse",),
                "fields": ("author", "is_published"),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        obj.save()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "date_posted", "approved_comment","rating"]
    list_filter = ["author", "date_posted", "approved_comment"]
    search_fields = ["author", "date_posted", "approved_comment"]


@admin.register(SocialModel)
class SocialModelAdmin(admin.ModelAdmin):
    list_display = ["id", "link", "icon"]
    list_filter = ["id", "link"]
    search_fields = ["id", "link"]
    list_editable = [
        "link",
        "icon",
    ]








