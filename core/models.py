'''
File: models.py
Description:
    Database models for the Blogger platform.

Models:
    - Profile
    - Post
    - Comment
'''

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    '''
    User profile model.

    Attributes:
        user: Linked Django user.
        display_name: Public display name.
        bio_ar: Arabic bio.
        bio_en: English bio.
        avatar: Profile image.
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=150, blank=True)
    bio_ar = models.TextField(blank=True)
    bio_en = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        '''
        Return readable profile name.
        '''
        return self.user.username


class Post(models.Model):
    '''
    Blog post model.

    Attributes:
        author: User who created the post.
        title_ar: Arabic title.
        title_en: English title.
        content_ar: Arabic content.
        content_en: English content.
        cover_image: Optional post image.
        video: Optional post video.
        is_published: Publish status.
        published_at: Creation date.
    '''

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title_ar = models.CharField(max_length=2048)
    title_en = models.CharField(max_length=2048)
    content_ar = models.TextField()
    content_en = models.TextField()
    cover_image = models.ImageField(upload_to='posts/covers/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Model metadata.
        '''
        ordering = ['-published_at']

    def __str__(self):
        '''
        Return readable post title.
        '''
        return self.title_ar

    def get_absolute_url(self):
        '''
        Return post detail URL.
        '''
        return reverse('core:post_detail', args=[self.id])

    def get_title(self, lang='ar'):
        '''
        Return localized post title.

        Args:
            lang: Current language code.

        Returns:
            str: Arabic or English title.
        '''
        return self.title_ar if lang == 'ar' else self.title_en

    def get_content(self, lang='ar'):
        '''
        Return localized post content.

        Args:
            lang: Current language code.

        Returns:
            str: Arabic or English content.
        '''
        return self.content_ar if lang == 'ar' else self.content_en


class Comment(models.Model):
    '''
    Comment model for posts.

    Attributes:
        post: Related post.
        author: User who wrote the comment.
        content: Comment text.
        created_at: Comment creation datetime.
    '''

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Model metadata.
        '''
        ordering = ['-created_at']

    def __str__(self):
        '''
        Return readable comment label.
        '''
        return f'{self.author.username} - {self.post.title_ar}'