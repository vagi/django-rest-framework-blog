from rest_framework import routers
from .api import CategoryViewSet


router = routers.DefaultRouter()
router.register('api/category', CategoryViewSet, 'category')

urlpatterns = router.urls
