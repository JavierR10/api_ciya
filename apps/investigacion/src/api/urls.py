from rest_framework.routers import DefaultRouter
from apps.investigacion.src.api.sublinea.views import SublineaViewSet
from apps.investigacion.src.api.linea.views import LineaViewSet
from apps.investigacion.src.api.paisBm.views import PaisBmViewSet
from apps.investigacion.src.api.paisSv.views import PaisSvViewSet
from apps.investigacion.src.api.projectType.views import ProjectTypeViewSet
from apps.investigacion.src.api.group.views import GroupViewSet
from apps.investigacion.src.api.equipment.views import EquipmentViewSet
from apps.investigacion.src.api.topicBank.views import TopicBankViewSet
from apps.investigacion.src.api.convocatory.views import ConvocatoryViewSet
from apps.investigacion.src.api.project.views import ProjectViewSet


router = DefaultRouter()
router.register('sublinea', SublineaViewSet, basename='sublinea')
router.register('linea', LineaViewSet, basename='linea')
router.register('pais-bm', PaisBmViewSet, basename='pais-bm')
router.register('pais-sv', PaisSvViewSet, basename='pais-sv')
router.register('projectType', ProjectTypeViewSet, basename='projectType')
router.register('group', GroupViewSet, basename='group')
router.register('equipment', EquipmentViewSet, basename='equipment')
router.register('topicBank', TopicBankViewSet, basename='topicBank')
router.register('convocatory', ConvocatoryViewSet, basename='convocatory')
router.register('project', ProjectViewSet, basename='project')


urlpatterns = router.urls