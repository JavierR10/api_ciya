import django_filters
from apps.bonding.src.models.agreement import Agreement
from apps.bonding.src.models.careerAgreement import CareerAgreement
from apps.bonding.src.models.commissioner import Commissioner
from apps.bonding.src.models.commissionerVin import CommissionerVin
from apps.bonding.src.models.company import Company
from apps.bonding.src.models.documentsVin import DocumentsVin
from apps.bonding.src.models.documets import Documents
from apps.bonding.src.models.groupVin import GroupVin
from apps.bonding.src.models.integranteVIn import IntegranteVin
from apps.bonding.src.models.process import Process
from apps.bonding.src.models.processVin import ProcessVin
from apps.bonding.src.models.programVin import ProgramVin
from apps.bonding.src.models.projectVin import ProjectVin
from apps.bonding.src.models.registrationVin import RegistrationVin
from apps.bonding.src.models.scheduleVin import ScheduleVin
from apps.bonding.src.models.tutorVin import TutorVin
from apps.bonding.src.models.type import Type
from apps.bonding.src.models.typeVin import TypeVin


class NewsFilterAgreement(django_filters.FilterSet):
    class Meta:
        model = Agreement
        fields = {
            'id_con': ['exact'],
            'documento_con': ['icontains'],
            'fecha_inicio_con': ['exact', 'gte', 'lte'],
            'fecha_fin_con': ['exact', 'gte', 'lte'],
            'fk_id_emp': ['exact'],
            'fecha_creacion_con': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_con': ['exact', 'gte', 'lte'],
            'usuario_creacion_con': ['exact', 'icontains'],
            'usuario_actualizacion_con': ['exact', 'icontains'],
            'tipo_con': ['exact', 'icontains'],
            'estado_con': ['exact'],
        }

class NewsFilterCareerAgreement(django_filters.FilterSet):
    class Meta:
        model = CareerAgreement
        fields = {
            'id_con_car': ['exact'],
            'fk_id_con': ['exact'],
            'fk_id_car': ['exact'],
        }

class NewsFilterCommissioner(django_filters.FilterSet):
    class Meta:
        model = Commissioner
        fields = {
            'id_comi': ['exact'],
            'estado_comi': ['exact'],
            'fecha_creacion_comi': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_comi': ['exact', 'gte', 'lte'],
            'usuario_creacion_comi': ['exact', 'icontains'],
            'usuario_actualizacion_comi': ['exact', 'icontains'],
            'fk_id_doc': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_car': ['exact'],
        }

class NewsFilterCommissionerVin(django_filters.FilterSet):
    class Meta:
        model = CommissionerVin
        fields = {
            'id_comi': ['exact'],
            'estado_comi': ['exact'],
            'fecha_creacion_comi': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_comi': ['exact', 'gte', 'lte'],
            'usuario_creacion_comi': ['exact', 'icontains'],
            'usuario_actualizacion_comi': ['exact', 'icontains'],
            'fk_id_doc': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_car': ['exact'],
        }

class NewsFilterCompany(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = {
            'ruc_emp': ['exact', 'icontains'],
            'nombre_emp': ['icontains'],
            'provincia_emp': ['exact', 'icontains'],
            'canton_emp': ['exact', 'icontains'],
            'direccion_emp': ['icontains'],
            'latitud_emp': ['exact', 'gte', 'lte'],
            'longitud_emp': ['exact', 'gte', 'lte'],
            'telefono_emp': ['exact', 'icontains'],
            'correo_emp': ['exact', 'icontains'],
            'logo_emp': ['exact', 'icontains'],
            'tipo_emp': ['exact', 'icontains'],
            'estado_emp': ['exact', 'icontains'],
            'fecha_creacion_emp': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_emp': ['exact', 'gte', 'lte'],
            'usuario_creacion_emp': ['exact', 'icontains'],
            'usuario_actualizacion_emp': ['exact', 'icontains'],
            'parroquia_emp': ['exact', 'icontains'],
            'actividad_emp': ['icontains'],
            'sector_economico_emp': ['icontains'],
        }

class NewsFilterDocumentsVin(django_filters.FilterSet):
    class Meta:
        model = DocumentsVin
        fields = {
            'id_doc': ['exact'],
            'nombre_doc': ['icontains'],
            'descripcion_doc': ['icontains'],
            'estado_doc': ['exact'],
            'fecha_creacion_doc': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_doc': ['exact', 'gte', 'lte'],
            'usuario_creacion_doc': ['exact', 'icontains'],
            'usuario_actualizacion_doc': ['exact', 'icontains'],
            'documento_doc': ['exact', 'icontains'],
            'fk_id_proy': ['exact'],
        }
class NewsFilterDocuments(django_filters.FilterSet):
    class Meta:
        model = Documents
        fields = {
            'id_doc': ['exact'],
            'nombre_doc': ['icontains'],
            'descripcion_doc': ['icontains'],
            'fecha_creacion_doc': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_doc': ['exact', 'gte', 'lte'],
            'usuario_creacion_doc': ['exact', 'icontains'],
            'usuario_actualizacion_doc': ['exact', 'icontains'],
            'documento_doc': ['exact', 'icontains'],
        }

class NewsFilterGroupVin(django_filters.FilterSet):
    class Meta:
        model = GroupVin
        fields = {
            'id_grupo': ['exact'],
            'nombre_grupo': ['icontains'],
            'numero_grupo': ['icontains'],
            'estado_grupo': ['exact'],
            'fecha_creacion_grupo': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_grupo': ['exact', 'gte', 'lte'],
            'usuario_creacion_grupo': ['exact', 'icontains'],
            'usuario_actualizacion_grupo': ['exact', 'icontains'],
            'fk_id_prov': ['exact'],
            'fk_id_con': ['exact'],
            'fk_id_cur': ['exact'],
            'fk_id_emp': ['exact'],
        }

class NewsFilterIntegranteVin(django_filters.FilterSet):
    class Meta:
        model = IntegranteVin
        fields = {
            'id_inte': ['exact'],
            'estado_inte': ['exact'],
            'fecha_creacion_inte': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_inte': ['exact', 'gte', 'lte'],
            'usuario_creacion_inte': ['exact', 'icontains'],
            'usuario_actualizacion_inte': ['exact', 'icontains'],
            'fk_id_grupo': ['exact'],
            'fk_id_matr': ['exact'],
        }

class NewsFilterProcess(django_filters.FilterSet):
    class Meta:
        model = Process
        fields = {
            'id_proc': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_tip': ['exact'],
            'fk_id_con': ['exact'],
            'fk_id_doc': ['exact'],
            'tema_proc': ['icontains'],
            'fecha_creacion_proc': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_proc': ['exact', 'gte', 'lte'],
            'usuario_creacion_proc': ['exact', 'icontains'],
            'usuario_actualizacion_proc': ['exact', 'icontains'],
        }

class NewsFilterProcessVin(django_filters.FilterSet):
    class Meta:
        model = ProcessVin
        fields = {
            'id_prov': ['exact'],
            'nombre_prov': ['icontains'],
            'descripcion_prov': ['icontains'],
            'estado_prov': ['exact'],
            'fecha_creacion_prov': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_prov': ['exact', 'gte', 'lte'],
            'usuario_creacion_prov': ['exact', 'icontains'],
            'usuario_actualizacion_prov': ['exact', 'icontains'],
            'fk_id_proy': ['exact'],
            'fk_id_tipo': ['exact'],
            'fk_id_doc': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_car': ['exact'],
            'fk_id_cur': ['exact'],
            'fk_id_tut': ['exact'],
        }

class NewsFilterProgramVin(django_filters.FilterSet):
    class Meta:
        model = ProgramVin
        fields = {
            'id_prog': ['exact'],
            'nombre_prog': ['icontains'],
            'descripcion_prog': ['icontains'],
            'estado_prog': ['exact'],
            'fecha_creacion_prog': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_prog': ['exact', 'gte', 'lte'],
            'usuario_creacion_prog': ['exact', 'icontains'],
            'usuario_actualizacion_prog': ['exact', 'icontains'],
            'fk_id_fac': ['exact'],
            'archivo_prog': ['exact', 'icontains'],
        }

class NewsFilterProjectVin(django_filters.FilterSet):
    class Meta:
        model = ProjectVin
        fields = {
            'id_proy': ['exact'],
            'nombre_proy': ['icontains'],
            'descripcion_proy': ['icontains'],
            'estado_proy': ['exact'],
            'fecha_creacion_proy': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_proy': ['exact', 'gte', 'lte'],
            'usuario_creacion_proy': ['exact', 'icontains'],
            'usuario_actualizacion_proy': ['exact', 'icontains'],
            'fk_id_car': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_prog': ['exact'],
        }

class NewsFilterRegistrationVin(django_filters.FilterSet):
    class Meta:
        model = RegistrationVin
        fields = {
            'id_matr': ['exact'],
            'estado_matr': ['exact'],
            'fecha_creacion_matr': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_matr': ['exact', 'gte', 'lte'],
            'usuario_creacion_matr': ['exact', 'icontains'],
            'usuario_actualizacion_matr': ['exact', 'icontains'],
            'fk_id_est': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_tipo': ['exact'],
            'fk_id_car': ['exact'],
            'fk_id_cur': ['exact'],
        }

class NewsFilterScheduleVin(django_filters.FilterSet):
    class Meta:
        model = ScheduleVin
        fields = {
            'id_cro': ['exact'],
            'semanauno_cro': ['icontains'],
            'semanados_cro': ['icontains'],
            'semanatres_cro': ['icontains'],
            'semanacuatro_cro': ['icontains'],
            'semanacinco_cro': ['icontains'],
            'semanaseis_cro': ['icontains'],
            'semanasiete_cro': ['icontains'],
            'semanaocho_cro': ['icontains'],
            'semananueve_cro': ['icontains'],
            'semanadiez_cro': ['icontains'],
            'semanaonce_cro': ['icontains'],
            'semanadose_cro': ['icontains'],
            'semanatrese_cro': ['icontains'],
            'semanacatorse_cro': ['icontains'],
            'semanaquinse_cro': ['icontains'],
            'semanadiecises_cro': ['icontains'],
            'estado_cro': ['exact'],
            'fecha_creacion_cro': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_cro': ['exact', 'gte', 'lte'],
            'usuario_creacion_cro': ['exact', 'icontains'],
            'usuario_actualizacion_cro': ['exact', 'icontains'],
            'fk_id_prf': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_car': ['exact'],
            'fk_id_est': ['exact'],
            'fk_id_doc': ['exact'],
        }

class NewsFilterTutorVin(django_filters.FilterSet):
    class Meta:
        model = TutorVin
        fields = {
            'id_tut': ['exact'],
            'estado_tut': ['exact'],
            'fecha_creacion_tut': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_tut': ['exact', 'gte', 'lte'],
            'usuario_creacion_tut': ['exact', 'icontains'],
            'usuario_actualizacion_tut': ['exact', 'icontains'],
            'fk_id_doc': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_tipo': ['exact'],
            'fk_id_car': ['exact'],
            'fk_id_cur': ['exact'],
        }

class NewsFilterType(django_filters.FilterSet):
    class Meta:
        model = Type
        fields = {
            'id_tip': ['exact'],
            'nombre_tip': ['icontains'],
            'siglas_tip': ['exact', 'icontains'],
            'estado_tip': ['exact'],
            'fecha_creacion_tip': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_tip': ['exact', 'gte', 'lte'],
            'usuario_creacion_tip': ['exact', 'icontains'],
            'usuario_actualizacion_tip': ['exact', 'icontains'],
        }

class NewsFilterTypeVin(django_filters.FilterSet):
    class Meta:
        model = TypeVin
        fields = {
            'id_tipo': ['exact'],
            'nombre_tipo': ['icontains'],
            'siglas_tipo': ['exact', 'icontains'],
            'descripcion_tipo': ['icontains'],
            'estado_tipo': ['exact'],
            'fecha_creacion_tipo': ['exact', 'gte', 'lte'],
            'fecha_actualizacion_tipo': ['exact', 'gte', 'lte'],
            'usuario_creacion_tipo': ['exact', 'icontains'],
            'usuario_actualizacion_tipo': ['exact', 'icontains'],
        }
