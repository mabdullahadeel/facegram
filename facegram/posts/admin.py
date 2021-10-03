from django.contrib import admin
from facegram.posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'author__username')

admin.site.register(Post, PostAdmin)
