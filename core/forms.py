'''
File: forms.py
Description:
    Forms for authentication, profile management,
    posts, and comments.
'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Profile


class RegisterForm(UserCreationForm):
    '''
    User registration form.
    '''
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email',
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Username',
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Password',
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirm Password',
        })
    )

    class Meta:
        '''
        Register form metadata.
        '''
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    '''
    Form for updating basic user account info.
    '''

    class Meta:
        '''
        User update form metadata.
        '''
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'اسم المستخدم / Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'البريد الإلكتروني / Email',
            }),
        }


class ProfileForm(forms.ModelForm):
    '''
    Form for updating user profile.
    '''

    class Meta:
        '''
        Profile form metadata.
        '''
        model = Profile
        fields = ['display_name', 'bio_ar', 'bio_en', 'avatar']
        widgets = {
            'display_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'الاسم الظاهر / Display name',
            }),
            'bio_ar': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 5,
                'placeholder': 'اكتب نبذتك بالعربية',
            }),
            'bio_en': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 5,
                'placeholder': 'Write your bio in English',
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-file',
            }),
        }


class PostForm(forms.ModelForm):
    '''
    Form for creating and updating posts.
    '''

    class Meta:
        '''
        Post form metadata.
        '''
        model = Post
        fields = [
            'title_ar',
            'title_en',
            'content_ar',
            'content_en',
            'cover_image',
            'video',
            'is_published',
        ]
        widgets = {
            'title_ar': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'عنوان المقال بالعربية',
            }),
            'title_en': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Post title in English',
            }),
            'content_ar': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 8,
                'placeholder': 'اكتب المحتوى بالعربية',
            }),
            'content_en': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 8,
                'placeholder': 'Write the content in English',
            }),
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'form-file',
            }),
            'video': forms.ClearableFileInput(attrs={
                'class': 'form-file',
            }),'is_published': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
        }


class CommentForm(forms.ModelForm):
    '''
    Form for post comments.
    '''

    class Meta:
        '''
        Comment form metadata.
        '''
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-textarea comment-textarea',
                'rows': 4,
                'placeholder': 'اكتب تعليقك هنا / Write your comment here',
            }),
        }