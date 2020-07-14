from rest_framework import routers
from .api import ListViewSet

router = routers.DefaultRouter()
router.register('api/lists', ListViewSet, 'lists')

urlpatterns = router.urls
