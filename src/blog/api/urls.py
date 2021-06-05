from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('post/new/', views.PostCreateView.as_view()),
]
