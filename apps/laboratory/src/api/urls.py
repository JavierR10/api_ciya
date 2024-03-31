from rest_framework.routers import DefaultRouter
from apps.laboratory.src.api.reservationType.views import ReservationTypeViewSet
from apps.laboratory.src.api.software.views import SoftwareViewSet
from apps.laboratory.src.api.area.views import AreaViewSet

router = DefaultRouter()
router.register('reservationType', ReservationTypeViewSet, basename='reservationType')
router.register('software', SoftwareViewSet, basename='software')
router.register('areas', AreaViewSet, basename='areas')

urlpatterns = router.urls