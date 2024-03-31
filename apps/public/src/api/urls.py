from rest_framework.routers import DefaultRouter
from apps.public.src.api.university.views import UniversityViewSet
from apps.public.src.api.profile.views import ProfileViewSet
from apps.public.src.api.usuario.views import UsersViewSet
from apps.public.src.api.profileUsers.views import ProfileUsersViewSet
from apps.public.src.api.teacher.views import TeacherViewSet
from apps.public.src.api.collegeCareer.views import CollegeCareerViewSet

router = DefaultRouter()
router.register('university', UniversityViewSet, basename='university')
router.register('profile', ProfileViewSet, basename='profile')
router.register('users', UsersViewSet, basename='users')
router.register('profileUsers', ProfileUsersViewSet, basename='profileUsers')
router.register('teacher', TeacherViewSet, basename='teacher')
router.register('collegeCareer', CollegeCareerViewSet, basename='collegeCareer')

urlpatterns = router.urls