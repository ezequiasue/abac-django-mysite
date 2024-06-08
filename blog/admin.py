from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
    search_fields = ('title', 'author')
    list_filter = ('created_on', 'author')
    autocomplete_fields = ('author',)
    
admin.site.register(Post,PostAdmin)