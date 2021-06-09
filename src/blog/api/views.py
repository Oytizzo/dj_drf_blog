from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from blog.models import Post
from .serializers import PostSerializer, PostInputSerializer
from .paginations import LargeResultsSetPagination, StandardResultsSetPagination


class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination


class UserPostListView(ListAPIView):
    pass


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostInputSerializer


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostInputSerializer


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
