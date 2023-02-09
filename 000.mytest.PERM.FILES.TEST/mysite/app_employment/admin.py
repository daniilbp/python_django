from django.contrib import admin
from app_employment.models import Vacancy, Resume


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Vacancy, VacancyAdmin)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

    def user_verbose(self, obj: Resume) -> str:
        return obj.user.first_name or obj.user.username
