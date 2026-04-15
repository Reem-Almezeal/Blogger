<!--
'''
File: profile.html
Description:
    User dashboard page for managing profile and posts.

Features:
    - User info section
    - My posts grid
    - Edit profile button
    - Create post button
    - View / edit / delete actions
'''
-->
{% extends 'core/base.html' %}
{% load static %}

{% block title %}
    {% if current_lang == 'en' %}My Profile | Blogger{% else %}حسابي | Blogger{% endif %}
{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'css/posts.css' %}">
<link rel="stylesheet" href="{% static 'css/profile.css' %}">
{% endblock %}

{% block content %}

<!-- Profile -->
<section class="profile-hero">
    <div class="container">
        <div class="profile-card reveal-up">

            <div class="profile-avatar-wrapper">
                {% if request.user.profile.avatar %}
                    <img src="{{ request.user.profile.avatar.url }}" alt="{{ request.user.username }}" class="profile-avatar">
                {% else %}
                    <div class="profile-avatar placeholder-avatar">
                        {{ request.user.username|first|upper }}
                    </div>
                {% endif %}
            </div>

            <div class="profile-info">
                <span class="section-subtitle">
                    {% if current_lang == 'en' %}My Dashboard{% else %}لوحة التحكم الخاصة بي{% endif %}
                </span>

                <h1>
                    {% if request.user.profile.display_name %}
                        {{ request.user.profile.display_name }}
                    {% else %}
                        {{ request.user.username }}
                    {% endif %}
                </h1>

                <p>
                    {% if current_lang == 'en' %}
                        {% if request.user.profile.bio_en %}
                            {{ request.user.profile.bio_en }}
                        {% else %}
                            Add your English bio from the edit profile page.
                        {% endif %}
                    {% else %}
                        {% if request.user.profile.bio_ar %}
                            {{ request.user.profile.bio_ar }}
                        {% else %}
                            أضيفي نبذتك الشخصية من صفحة تعديل الحساب.
                        {% endif %}
                    {% endif %}
                </p>

                <div class="profile-actions">
                    <a href="{% url 'core:edit_profile' %}?lang={{ current_lang }}" class="secondary-btn">
                        {% if current_lang == 'en' %}Edit Profile{% else %}تعديل الحساب{% endif %}
                    </a>

                    <a href="/posts/create/?lang={{ current_lang }}" class="primary-btn">
                        {% if current_lang == 'en' %}Create Post{% else %}إضافة مقال{% endif %}
                    </a>
                </div>
            </div>

        </div>
    </div>
</section>

<!-- my posts section -->
<section class="posts-list-section">
    <div class="container">

        <!-- header section -->
        <div class="section-head reveal-up">
            <div>
                <span class="section-subtitle">
                    {% if current_lang == 'en' %}My Articles{% else %}مقالاتي{% endif %}
                </span>
            </div>
        </div>

    </div>
</section>

{% endblock %}