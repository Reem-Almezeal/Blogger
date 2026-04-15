from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='core:home'),name='logout'),
    path('profile/', views.my_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('author/<str:username>/', views.author_profile, name='author_profile'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/edit/', views.post_update, name='post_update'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]