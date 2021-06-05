from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from blog.models import Post
from .serializers import PostSerializer
from .paginations import LargeResultsSetPagination, StandardResultsSetPagination


class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
