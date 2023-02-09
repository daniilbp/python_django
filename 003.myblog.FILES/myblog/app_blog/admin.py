from django.contrib import admin

from app_blog.models import Post, File


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = "id", "title", "user", "created_at"

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def user_verbose(self, obj: Post) -> str:
        return obj.user.first_name or obj.user.username


admin.site.register(Post, PostAdmin)


class FileAdmin(admin.ModelAdmin):
    list_display = "id", "file"


admin.site.register(File, FileAdmin)
