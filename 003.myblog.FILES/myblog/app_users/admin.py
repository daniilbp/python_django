from django.contrib import admin
from app_users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'avatar_tag', 'user', 'name', 'surname', 'num_posts')
    readonly_fields = ['avatar_tag']
    fields = ('avatar_tag', 'avatar', 'user', 'name', 'surname', 'num_posts')


admin.site.register(Profile, ProfileAdmin)
