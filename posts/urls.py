"""Posts URLs"""

# Django
from django.urls import path, include
from django.contrib.auth.decorators import login_required

# Views
from posts import views
from .views import post_view, like_post

app_name = 'posts'

urlpatterns = [
    path(
        route='',
        view=login_required(views.PostFeedView.as_view()),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create_post'
    ),

    path(
        route='posts/<int:post_id>/',
        view=login_required(views.PostDetailView.as_view()),
        name='detail'
    ),
    path('', post_view, name='post-list'),
    path('like/', like_post, name='like-post'),
]
