from rest_framework.routers import DefaultRouter

from .views import MainCategoryViewSet, MiddleCategoryViewSet, SubCategoryViewSet


router = DefaultRouter()

router.register('main', MainCategoryViewSet)
router.register('middle', MiddleCategoryViewSet)
router.register('sub', SubCategoryViewSet)

urlpatterns = router.urls
