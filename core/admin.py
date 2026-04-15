

from django.contrib import admin
from .models import Profile, Post, Comment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''
    Admin settings for Profile model.
    '''
    list_display = ('user', 'display_name')
    search_fields = ('user__username', 'display_name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''
    Admin settings for Post model.
    '''
    list_display = ('title_ar', 'title_en', 'author', 'is_published', 'published_at')
    list_filter = ('is_published', 'published_at')
    search_fields = ('title_ar', 'title_en', 'content_ar', 'content_en', 'author__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Admin settings for Comment model.
    '''
    list_display = ('author', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'content', 'post__title_ar', 'post__title_en')