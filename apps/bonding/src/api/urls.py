from rest_framework.routers import DefaultRouter
from apps.bonding.src.api.agreement.views import AgreementViewSet
from apps.bonding.src.api.careerAgreement.views import CareerAgreementViewSet
from apps.bonding.src.api.commissioner.views import CommissionerViewSet
from apps.bonding.src.api.commissionerVin.views import CommissionerVinViewSet
from apps.bonding.src.api.company.views import CompanyViewSet
from apps.bonding.src.api.documentsVin.views import DocumentsVinViewSet
from apps.bonding.src.api.documets.views import DocumentsViewSet
from apps.bonding.src.api.groupVin.views import GroupVinViewSet
from apps.bonding.src.api.integranteVIn.views import IntegranteVinViewSet
from apps.bonding.src.api.process.views import ProcessViewSet
from apps.bonding.src.api.processVin.views import ProcessVinProcessViewSet
from apps.bonding.src.api.programVin.views import ProgramVinViewSet
from apps.bonding.src.api.projectVin.views import ProjectVinViewSet
from apps.bonding.src.api.registrationVin.views import RegistrationVinViewSet
from apps.bonding.src.api.scheduleVin.views import ScheduleVinViewSet
from apps.bonding.src.api.tutorVin.views import TutorVinViewSet
from apps.bonding.src.api.type.views import TypeViewSet
from apps.bonding.src.api.typeVin.views import TypeVinViewSet



router = DefaultRouter()
router.register('agreement',AgreementViewSet, basename='agreement')
router.register('careerAgreement',CareerAgreementViewSet, basename='careerAgreement')
router.register('commissioner',CommissionerViewSet, basename='commissioner')
router.register('commissionerVin',CommissionerVinViewSet, basename='commissionerVin')
router.register('company',CompanyViewSet , basename='company')
router.register('documentsVin',DocumentsVinViewSet, basename='documentsVin')
router.register('documets',DocumentsViewSet, basename='documets')
router.register('groupVin',GroupVinViewSet, basename='groupVin')
router.register('integranteVIn',IntegranteVinViewSet, basename='integranteVIn')
router.register('process',ProcessViewSet, basename='process')
router.register('processVin',ProcessVinProcessViewSet, basename='processVin')
router.register('programVin',ProgramVinViewSet, basename='programVin')
router.register('projectVin',ProjectVinViewSet, basename='projectVin')
router.register('registrationVin',RegistrationVinViewSet, basename='registrationVin')
router.register('scheduleVin',ScheduleVinViewSet, basename='scheduleVin')
router.register('tutorVin',TutorVinViewSet, basename='tutorVin')
router.register('type',TypeViewSet, basename='type')
router.register('typeVin',TypeVinViewSet, basename='typeVin')



urlpatterns = router.urls