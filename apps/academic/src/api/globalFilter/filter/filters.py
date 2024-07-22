import django_filters
from apps.academic.src.models.associatedDocument import AssociatedDocument
from apps.academic.src.models.attach import Attach
from apps.academic.src.models.collaborator import Collaborator
from apps.academic.src.models.documents import Documents
from apps.academic.src.models.folder import Folder
from apps.academic.src.models.news import News

class NewsFilterAssociatedDocument(django_filters.FilterSet):
    class Meta:
        model = AssociatedDocument
        fields = {
            'id_aso': ['exact'],
            'fk_id_doc': ['exact'],
            'fk_id_doc_asociado': ['exact'],
        }
class NewsFilterAttach(django_filters.FilterSet):
    class Meta:
        model = Attach
        fields = {
            'id_adj': ['exact'],
            'fk_id_not': ['exact'],
            'nombre_adj': ['icontains'],
            'documento_adj': ['exact'],
            'fecha_subida_adj': ['lte', 'gte'],
        }
class NewsFilterCollaborator(django_filters.FilterSet):
    class Meta:
        model = Collaborator
        fields = {
            'id_col': ['exact'],
            'fk_id_carp': ['exact'],
            'fk_id_usu': ['exact'],
            'entrega_col': ['exact'],
            'notificacion_col': ['exact'],
            'acceso_col': ['exact'],
        }
class NewsFilterDocuments(django_filters.FilterSet):
    class Meta:
        model = Documents
        fields = {
            'id_doc': ['exact'],
            'fk_id_carp': ['exact'],
            'nombre_doc': ['icontains'],
            'documento_doc': ['exact'],
            'descripcion_doc': ['icontains'],
            'fecha_entrega_doc': ['lte', 'gte'],
            'fecha_creacion_doc': ['lte', 'gte'],
            'fecha_actualizacion_doc': ['lte', 'gte'],
            'usuario_creacion_doc': ['exact'],
            'usuario_actualizacion_doc': ['exact'],
            'fk_id_usu': ['exact'],
            'publico_doc': ['exact'],
        }
class NewsFilterFolder(django_filters.FilterSet):
    class Meta:
        model = Folder
        fields = {
            'id_carp': ['exact'],
            'parend_id_carp': ['exact'],
            'nombre_carp': ['icontains'],
            'fk_id_usu': ['exact'],
            'descripcion_carp': ['icontains'],
            'fecha_cierre_carp': ['lte', 'gte'],
            'hora_cierre_carp': ['lte', 'gte'],
            'estado_carp': ['exact'],
            'disposicion_carp': ['exact'],
            'fecha_creacion_carp': ['lte', 'gte'],
            'fecha_actualizacion_carp': ['lte', 'gte'],
        }
class NewsFilterNews(django_filters.FilterSet):
    class Meta:
        model = News
        fields = {
            'id_not': ['exact'],
            'titulo_not': ['icontains'],
            'descripcion_not': ['icontains'],
            'imagen_not': ['exact'],
            'estado_not': ['exact'],
            'fecha_creacion_not': ['lte', 'gte'],
        }