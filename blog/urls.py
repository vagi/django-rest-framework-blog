from rest_framework import routers
from .api import CategoryViewSet


router = routers.DefaultRouter()
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls
