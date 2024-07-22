from rest_framework.routers import DefaultRouter
from apps.public.src.api.academicMesh.views import AcademicMeshViewSet
from apps.public.src.api.careerArea.views import CareerAreaViewSet
from apps.public.src.api.collegeCareer.views import CollegeCareerViewSet
from apps.public.src.api.counter.views import CounterViewSet
from apps.public.src.api.course.views import CourseViewSet
from apps.public.src.api.distributive.views import DistributiveViewSet
from apps.public.src.api.faculty.views import FacultyViewSet
from apps.public.src.api.individualSchedule.views import IndividualScheduleViewSet
from apps.public.src.api.matter.views import MatterViewSet
from apps.public.src.api.modules.views import ModuleViewSet
from apps.public.src.api.period.views import PeriodViewSet
from apps.public.src.api.permissions.views import PermissionsViewSet
from apps.public.src.api.profile.views import ProfileViewSet
from apps.public.src.api.profileUsers.views import ProfileUsersViewSet
from apps.public.src.api.security.views import SecurityViewSet
from apps.public.src.api.studentRepresentatives.views import StudentRepresentativesViewSet
from apps.public.src.api.students.views import StudentsViewSet
from apps.public.src.api.teacher.views import TeacherViewSet
from apps.public.src.api.university.views import UniversityViewSet
from apps.public.src.api.usuario.views import UsersViewSet

router = DefaultRouter()
router.register('academicMesh',AcademicMeshViewSet, basename='academicMesh')
router.register('careerArea',CareerAreaViewSet, basename='careerArea')
router.register('collegeCareer',CollegeCareerViewSet, basename='collegeCareer')
router.register('counter',CounterViewSet, basename='counter')
router.register('course',CourseViewSet, basename='course')
router.register('distributive',DistributiveViewSet, basename='distributive')
router.register('faculty',FacultyViewSet, basename='faculty')
router.register('individualSchedule',IndividualScheduleViewSet, basename='individualSchedule')
router.register('matter',MatterViewSet, basename='matter')
router.register('modules',ModuleViewSet, basename='modules')
router.register('period',PeriodViewSet, basename='period')
router.register('permissions',PermissionsViewSet, basename='permissions')
router.register('profile',ProfileViewSet, basename='profile')
router.register('profileUsers',ProfileUsersViewSet, basename='profileUsers')
router.register('security',SecurityViewSet, basename='security')
router.register('studentRepresentatives',StudentRepresentativesViewSet, basename='studentRepresentatives')
router.register('students',StudentsViewSet, basename='students')
router.register('teacher',TeacherViewSet, basename='teacher')
router.register('university',UniversityViewSet, basename='university')
router.register('usuario',UsersViewSet, basename='usuario')

urlpatterns = router.urls