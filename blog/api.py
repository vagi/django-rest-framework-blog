from django.contrib.auth import logout
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Author, Post, Comment
from .serializers import CategorySerializer, AuthorSerializer, PostSerializer, CommentSerializer
from .mixin import CacheMixin
from .pagination import StandardResultsSetPagination


# Alternative approach of caching
#from django.views.decorators.cache import cache_page
#from django.utils.decorators import method_decorator

#@method_decorator(cache_page(60 * 5), name='dispatch')
#class CategoryViewSet(viewsets.ModelViewSet):


class CategoryViewSet(CacheMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter]
    filterset_fields = ['category']
    ordering_fields = ['category']


class AuthorViewSet(CacheMixin, viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter]
    filterset_fields = ['surname']
    ordering_fields = ['id', 'surname']


class PostViewSet(CacheMixin, viewsets.ModelViewSet):
    cache_timeout = 60 * 20
    queryset = Post.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = PostSerializer
    # Standard pagination that is set in pagination.py module
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter]     # [filters.SearchFilter] can be added if we want the search fields
    # This will show fields for filtering of posts.
    # Probably use of headline is not reasonable, for other fields you have a choice
    filterset_fields = ['author', 'category', 'headline']
    ordering_fields = ['id', 'headline', 'pub_date']


class CommentViewSet(CacheMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter]
    filterset_fields = ['post']
    ordering_fields = ['id', 'post', 'pub_date']


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
