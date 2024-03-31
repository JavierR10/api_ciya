from rest_framework.routers import DefaultRouter
from apps.laboratory.src.api.reservationType.views import ReservationTypeViewSet
from apps.laboratory.src.api.software.views import SoftwareViewSet
from apps.laboratory.src.api.area.views import AreaViewSet
from apps.laboratory.src.api.practicalGuide.views import PracticalGuideViewSet
from apps.laboratory.src.api.reservation.views import ReservationViewSet
from apps.laboratory.src.api.hoursExecuted.views import HoursExecutedViewSet
from apps.laboratory.src.api.laboratory.views import LaboratoryViewSet
from apps.laboratory.src.api.laboratorySoftware.views import LaboratorySoftwareViewSet
from apps.laboratory.src.api.areaLaboratory.views import AreaLaboratoryViewSet
from apps.laboratory.src.api.laboratoryCareer.views import LaboratoryCareerViewSet
from apps.laboratory.src.api.observationGuide.views import ObservationGuideViewSet
from apps.laboratory.src.api.softwareReservation.views import SoftwareReservationViewSet

router = DefaultRouter()
router.register('reservationType', ReservationTypeViewSet, basename='reservationType')
router.register('software', SoftwareViewSet, basename='software')
router.register('areas', AreaViewSet, basename='areas')
router.register('practicalGuide', PracticalGuideViewSet, basename='practicalGuide')
router.register('reservation', ReservationViewSet, basename='reservation')
router.register('hoursExecuted', HoursExecutedViewSet, basename='hoursExecuted')
router.register('laboratory', LaboratoryViewSet, basename='laboratory')
router.register('laboratorySoftware', LaboratorySoftwareViewSet, basename='laboratorySoftware')
router.register('areaLaboratory', AreaLaboratoryViewSet, basename='areaLaboratory')
router.register('laboratoryCareer', LaboratoryCareerViewSet, basename='laboratoryCareer')
router.register('observationGuide', ObservationGuideViewSet, basename='observationGuide')
router.register('softwareReservation', SoftwareReservationViewSet, basename='softwareReservation')

urlpatterns = router.urls