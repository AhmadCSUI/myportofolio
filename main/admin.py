from django.contrib import admin
from .models import Docs

@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
    list_display = ('title',)
