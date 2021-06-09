from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from blog.models import Post
from .serializers import PostSerializer, PostInputSerializer, UserPostSerializer
from .paginations import LargeResultsSetPagination, StandardResultsSetPagination


class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination


class UserPostListView(ListAPIView):
    serializer_class = UserPostSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostInputSerializer


class PostUpdateView(UserPassesTestMixin, UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostInputSerializer

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
