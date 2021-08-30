from django.contrib.auth import logout
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Category, Author, Post, Comment
from .serializers import CategorySerializer, AuthorSerializer, PostSerializer, CommentSerializer
from .mixin import CacheMixin

# Alternative approach of caching
#from django.views.decorators.cache import cache_page
#from django.utils.decorators import method_decorator

#@method_decorator(cache_page(60 * 5), name='dispatch')
#class CategoryViewSet(viewsets.ModelViewSet):


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
    cache_timeout = 60 * 20
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
