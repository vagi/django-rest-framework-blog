from rest_framework import routers
from .api import CategoryViewSet, AuthorViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('api/categories', CategoryViewSet, 'categories')
router.register('api/authors', AuthorViewSet, 'authors')
router.register('api/posts', PostViewSet, 'posts')
router.register('api/comments', CommentViewSet, 'comments')

urlpatterns = router.urls
