from django.contrib.auth import logout
from rest_framework import viewsets, permissions, status
from .serializers import CategorySerializer, AuthorSerializer, PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.cache import cache_page
from .models import Category, Author, Post, Comment


# This class implements cashing of choosen viewset with designed timeout
class CacheMixin(object):
    cache_timeout = 60 * 10

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)


class CategoryViewSet(CacheMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CategorySerializer



class AuthorViewSet(CacheMixin, viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AuthorSerializer


class PostViewSet(CacheMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostSerializer


class CommentViewSet(CacheMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CommentSerializer


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def user_logout(request):
    '''
    This method deletes current user's auth token via GET request,
    so the user will be logged out
    '''
    request.user.auth_token.delete()
    logout(request)
    return Response('User logged out successfully!')
