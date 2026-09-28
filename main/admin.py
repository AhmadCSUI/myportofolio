from django.contrib import admin
from main.models import Education, Experience


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'score', 'started_at', 'ended_at')
    list_filter = ('category',)
    search_fields = ('title',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'started_at', 'ended_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
