from django.contrib import admin
from facegram.posts.models import Post, PostComment, PostVotes, PostCommentVotes

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


class PostCommentVotesInline(admin.StackedInline):
    model = PostCommentVotes
    extra = 1


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('commenter__username',)
    inlines = [PostCommentVotesInline]


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostVotes)
admin.site.register(PostCommentVotes)
