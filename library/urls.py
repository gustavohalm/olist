from rest_framework import routers
from .views import AuthorViewSet, BookViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'authors/?', AuthorViewSet)
router.register(r'books/?', BookViewSet)

urlpatterns = router.urls
