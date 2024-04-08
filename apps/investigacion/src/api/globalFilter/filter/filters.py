import django_filters
from apps.investigacion.src.models.convocatory import Convocatory
from apps.investigacion.src.models.equipment import Equipment
from apps.investigacion.src.models.group import Group
from apps.investigacion.src.models.linea import Linea
from apps.investigacion.src.models.paisBm import PaisBm
from apps.investigacion.src.models.paisSv import PaisSv
from apps.investigacion.src.models.project import Project
from apps.investigacion.src.models.projectType import ProjectType
from apps.investigacion.src.models.sublinea import Sublinea
from apps.investigacion.src.models.topicBank import TopicBank

class NewsFilterConvocatory(django_filters.FilterSet):
    class Meta:
        model = Convocatory
        fields = {
            'id_conv': ['exact'],
            'documento_conv': ['exact'],
            'estado_conv': ['exact'],
        }

class NewsFilterEquipment(django_filters.FilterSet):
    class Meta:
        model = Equipment
        fields = {
            'id_equ': ['exact'],
            'fk_id_doc': ['exact'],
            'fk_id_gru': ['exact'],
        }

class NewsFilterGroup(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'id_gru': ['exact'],
            'nombre_gru': ['icontains'],
            'tipo_gru': ['exact'],
        }

class NewsFilterLinea(django_filters.FilterSet):
    class Meta:
        model = Linea
        fields = {
            'id_lin': ['exact'],
            'descripcion_lin': ['icontains'],
            'estado_lin': ['exact'],
            'nombre_lin': ['icontains'],
        }

class NewsFilterPaisBm(django_filters.FilterSet):
    class Meta:
        model = PaisBm
        fields = {
            'id_bm': ['exact'],
            'nombre_bm': ['icontains'],
            'continente_bm': ['icontains'],
        }

class NewsFilterPaisSv(django_filters.FilterSet):
    class Meta:
        model = PaisSv
        fields = {
            'id_sv': ['exact'],
            'nombre_sv': ['icontains'],
            'continente_sv': ['icontains'],
        }

class NewsFilterProject(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'id_pro': ['exact'],
            'nombre_pro': ['icontains'],
            'fk_id_car': ['exact'],
            'fk_id_doc': ['exact'],
            'grupo_investigacion_pro': ['icontains'],
            'programa_pro': ['icontains'],
            'fk_id_tip': ['exact'],
            'fecha_aprobacion_pro': ['exact'],
            'fk_id_lin': ['exact'],
        }

class NewsFilterProjectType(django_filters.FilterSet):
    class Meta:
        model = ProjectType
        fields = {
            'id_tip': ['exact'],
            'nombre_tip': ['icontains'],
        }

class NewsFilterSublinea(django_filters.FilterSet):
    class Meta:
        model = Sublinea
        fields = {
            'id_sub': ['exact'],
            'fk_id_car': ['exact'],
            'nombre_sub': ['icontains'],
            'descripcion_sub': ['icontains'],
            'estado_sub': ['exact'],
        }

class NewsFilterTopicBank(django_filters.FilterSet):
    class Meta:
        model = TopicBank
        fields = {
            'id_ban': ['exact'],
            'fk_id_doc': ['exact'],
            'fk_id_lin': ['exact'],
            'fk_id_sub': ['exact'],
            'tema_ban': ['icontains'],
            'descripcion_ban': ['icontains'],
            'archivo_adjunto_ban': ['icontains'],
            'fecha_creacion_ban': ['exact'],
            'fecha_actualizacion_ban': ['exact'],
            'usuario_creacion_ban': ['icontains'],
            'usuario_actualizacion_ban': ['icontains'],
            'validacion_ban': ['exact'],
            'estado_ban': ['exact'],
        }
