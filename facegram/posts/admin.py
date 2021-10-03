from django.contrib import admin
from facegram.posts.models import Post, PostComment, PostVotes


class PostCommentInline(admin.StackedInline):
    model = PostComment
    extra = 1


class PostVotesInline(admin.StackedInline):
    model = PostVotes
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'author__username')
    inlines = [PostCommentInline, PostVotesInline]

admin.site.register(Post, PostAdmin)
