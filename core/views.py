'''
File: views.py
Description:
    Contains all application views for posts, profiles,
    authentication, comments, and language-aware rendering.
'''

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Post
from .forms import RegisterForm, PostForm, CommentForm, ProfileForm, UserUpdateForm


def get_current_lang(request):
    lang = request.GET.get('lang') or request.session.get('site_lang', 'ar')
    if lang not in ['ar', 'en']:
        lang = 'ar'
    request.session['site_lang'] = lang
    return lang


def home(request):
    lang = get_current_lang(request)
    latest_posts = Post.objects.filter(is_published=True).order_by('-published_at')[:6]

    return render(request, 'core/home.html', {
        'latest_posts': latest_posts,
        'current_lang': lang,
    })


def post_list(request):
    lang = get_current_lang(request)
    query = request.GET.get('q', '')
    posts = Post.objects.filter(is_published=True)

    if query:
        posts = posts.filter(
            Q(title_ar__icontains=query) |
            Q(title_en__icontains=query) |
            Q(content_ar__icontains=query) |
            Q(content_en__icontains=query) |
            Q(author__username__icontains=query)
        )

    return render(request, 'core/post_list.html', {
        'posts': posts,
        'query': query,
        'current_lang': lang,
    })


def register_view(request):
    lang = get_current_lang(request)

    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(f"/?lang={lang}")
    else:
        form = RegisterForm()

    return render(request, 'core/register.html', {
        'form': form,
        'current_lang': lang,
    })


def author_profile(request, username):
    lang = get_current_lang(request)
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author, is_published=True)

    return render(request, 'core/author_profile.html', {
        'author_user': author,
        'posts': posts,
        'current_lang': lang,
    })


@login_required
def my_profile(request):
    lang = get_current_lang(request)
    my_posts = Post.objects.filter(author=request.user)

    return render(request, 'core/profile.html', {
        'my_posts': my_posts,
        'current_lang': lang,
    })


@login_required
def edit_profile(request):
    lang = get_current_lang(request)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(f"/profile/?lang={lang}")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'core/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'current_lang': lang,
    })


@login_required
def post_create(request):
    lang = get_current_lang(request)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(f'{post.get_absolute_url()}?lang={lang}')
    else:
        form = PostForm()

    return render(request, 'core/post_form.html', {
        'form': form,
        'page_title': 'إنشاء مقال' if lang == 'ar' else 'Create Post',
        'button_text': 'نشر المقال' if lang == 'ar' else 'Publish Post','current_lang': lang,
    })


@login_required
def post_update(request, post_id):
    lang = get_current_lang(request)
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'{post.get_absolute_url()}?lang={lang}')
    else:
        form = PostForm(instance=post)

    return render(request, 'core/post_form.html', {
        'form': form,
        'page_title': 'تعديل المقال' if lang == 'ar' else 'Edit Post',
        'button_text': 'حفظ التعديلات' if lang == 'ar' else 'Save Changes',
        'current_lang': lang,
    })


def post_detail(request, post_id):
    lang = get_current_lang(request)
    post = get_object_or_404(Post, id=post_id, is_published=True)
    comments = post.comments.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f'/login/?lang={lang}')

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(f'{post.get_absolute_url()}?lang={lang}')
    else:
        comment_form = CommentForm()

    return render(request, 'core/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'current_lang': lang,
    })


@login_required
def post_delete(request, post_id):
    lang = get_current_lang(request)
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        return redirect('core:post_detail', post_id=post.id)

    if request.method == 'POST':
        post.delete()
        return redirect('core:post_list')

    return render(request, 'core/post_delete.html', {
        'post': post,
        'current_lang': lang,
    })