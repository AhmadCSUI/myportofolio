from django.contrib import admin
<<<<<<< Updated upstream
from .models import Docs

@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
    list_display = ('title',)
=======
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title')
>>>>>>> Stashed changes
