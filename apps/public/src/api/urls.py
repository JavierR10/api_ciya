from rest_framework.routers import DefaultRouter
from apps.public.src.api.university.views import UniversityViewSet
from apps.public.src.api.profile.views import ProfileViewSet
from apps.public.src.api.usuario.views import UsersViewSet
from apps.public.src.api.profileUsers.views import ProfileUsersViewSet

router = DefaultRouter()
router.register('university', UniversityViewSet, basename='university')
router.register('profile', ProfileViewSet, basename='profile')
router.register('users', UsersViewSet, basename='users')
router.register('profileUsers', ProfileUsersViewSet, basename='profileUsers')
urlpatterns = router.urls