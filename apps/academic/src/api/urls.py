from rest_framework.routers import DefaultRouter
from apps.academic.src.api.attach.views import AttachViewSet
from apps.academic.src.api.folder.views import FolderViewSet
from apps.academic.src.api.collaborator.views import CollaboratorViewSet
from apps.academic.src.api.documents.views import DocumentsViewSet
from apps.academic.src.api.associatedDocument.views import AssociatedDocumentViewSet
from apps.academic.src.api.news.views import NewsViewSet

router = DefaultRouter()
router.register('attach', AttachViewSet, basename='attach')
router.register('folder', FolderViewSet, basename='folder')
router.register('collaborator', CollaboratorViewSet, basename='collaborator')
router.register('documents', DocumentsViewSet, basename='documents')
router.register('associatedDocument', AssociatedDocumentViewSet, basename='associatedDocument')
router.register('news', NewsViewSet, basename='news')

urlpatterns = router.urls