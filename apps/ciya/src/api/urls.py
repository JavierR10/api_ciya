from rest_framework.routers import DefaultRouter
from apps.ciya.src.api.university.views import UniversityViewSet

router = DefaultRouter()
router.register('university', UniversityViewSet, basename='university')
urlpatterns = router.urls