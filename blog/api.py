from django.contrib.auth import logout

from .models import Category, Author, Post, Comment
from rest_framework import viewsets, permissions, status
from .serializers import CategorySerializer, AuthorSerializer, PostSerializer, CommentSerializer
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.IsAuthenticated    # change to IsAuthenticated
    ]
    serializer_class = CategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AuthorSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CommentSerializer


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def Logout(request):
    '''
    This method deletes current user's auth token via GET request,
    so the user will be logged out
    '''
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')
