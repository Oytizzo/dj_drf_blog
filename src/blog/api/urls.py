from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('post/new/', views.PostCreateView.as_view()),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view()),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view()),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
]
