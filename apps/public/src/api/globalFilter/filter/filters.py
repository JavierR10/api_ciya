import django_filters
from apps.public.src.models.academicMesh import AcademicMesh
from apps.public.src.models.careerArea import CareerArea
from apps.public.src.models.collegeCareer import CollegeCareer
from apps.public.src.models.counter import Counter
from apps.public.src.models.course import Course
from apps.public.src.models.distributive import Distributive
from apps.public.src.models.faculty import Faculty
from apps.public.src.models.individualSchedule import IndividualSchedule
from apps.public.src.models.matter import Matter
from apps.public.src.models.modules import Module
from apps.public.src.models.period import Period
from apps.public.src.models.permissions import Permissions
from apps.public.src.models.profile import profile
from apps.public.src.models.profileUsers import profileUsers
from apps.public.src.models.security import Security
from apps.public.src.models.studentRepresentatives import StudentRepresentatives
from apps.public.src.models.students import Students
from apps.public.src.models.teacher import Teacher
from apps.public.src.models.university import universidad
from apps.public.src.models.usuario import users

class NewsFilterAcademicMesh(django_filters.FilterSet):
    class Meta:
        model = AcademicMesh
        fields = {
            'id_malla': ['exact'],
            'fk_id_car': ['exact'],
            'nombre_malla': ['icontains'],
            'descripcion_malla': ['icontains'],
            'estado_malla': ['icontains'],
            'archivo_malla': ['icontains'],
            'fecha_creacion_malla': ['exact'],
            'fecha_actualizacion_malla': ['exact'],
            'usuario_creacion_malla': ['icontains'],
            'usuario_actualizacion_malla': ['icontains'],
        }

class NewsFilterCareerArea(django_filters.FilterSet):
    class Meta:
        model = CareerArea
        fields = {
            'id_area_car': ['exact'],
            'nombre_area_car': ['icontains'],
            'descripcion_area_car': ['icontains'],
            'foto_area_car': ['icontains'],
            'fk_id_car': ['exact'],
            'fk_id_doc': ['exact'],
        }

class NewsFilterCollegeCareer(django_filters.FilterSet):
    class Meta:
        model = CollegeCareer
        fields = {
            'id_car': ['exact'],
            'fk_id_fac': ['exact'],
            'nombre_car': ['icontains'],
            'siglas_car': ['icontains'],
            'fk_director_doc': ['icontains'],
            'foto_logo_car': ['icontains'],
            'telefono_car': ['icontains'],
            'email_car': ['icontains'],
            'fecha_creacion_car': ['exact'],
            'fecha_actualizacion_car': ['exact'],
            'usuario_creacion_car': ['icontains'],
            'usuario_actualizacion_car': ['icontains'],
            'mision_car': ['icontains'],
            'vision_car': ['icontains'],
            'fk_dir_doc': ['exact'],
        }

class NewsFilterCounter(django_filters.FilterSet):
    class Meta:
        model = Counter
        fields = {
            'id_con': ['exact'],
            'fecha_con': ['exact'],
        }

class NewsFilterCourse(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'id_cur': ['exact'],
            'fk_id_malla': ['exact'],
            'nombre_cur': ['icontains'],
            'fecha_creacion_cur': ['exact'],
            'fecha_actualizacion_cur': ['exact'],
            'usuario_creacion_cur': ['icontains'],
            'usuario_actualizacion_cur': ['icontains'],
        }

class NewsFilterDistributive(django_filters.FilterSet):
    class Meta:
        model = Distributive
        fields = {
            'id_dis': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_mat': ['exact'],
            'fk_id_doc': ['exact'],
            'paralelo_dis': ['exact'],
            'silabo_dis': ['icontains'],
            'fecha_creacion_dis': ['exact'],
            'fecha_actualizacion_dis': ['exact'],
            'usuario': ['icontains'],
        }

class NewsFilterFaculty(django_filters.FilterSet):
    class Meta:
        model = Faculty
        fields = {
            'id_fac': ['exact'],
            'nombre_fac': ['icontains'],
            'siglas_fac': ['icontains'],
            'fk_decano_fac': ['exact'],
            'fk_vicedecano_fac': ['exact'],
            'correo_fac': ['icontains'],
            'telefono_fac': ['icontains'],
            'fecha_creacion_fac': ['exact'],
            'fecha_actualizacion_fac': ['exact'],
            'usuario_creacion_fac': ['icontains'],
            'usuario_actualizacion_fac': ['icontains'],
            'mision_fac': ['icontains'],
            'vision_fac': ['icontains'],
            'logo_fac': ['icontains'],
        }

class NewsFilterIndividualSchedule(django_filters.FilterSet):
    class Meta:
        model = IndividualSchedule
        fields = {
            'id_horaindi': ['exact'],
            'archivo_horaindi': ['icontains'],
            'fk_id_doc': ['exact'],
            'fk_id_per': ['exact'],
            'fecha_creacion_horaindi': ['exact'],
            'fecha_actualizacion_horaindi': ['exact'],
            'usuario_creacion_horaindi': ['icontains'],
            'usuario_actualizacion_horaindi': ['icontains'],
        }

class NewsFilterMatter(django_filters.FilterSet):
    class Meta:
        model = Matter
        fields = {
            'id_mat': ['exact'],
            'fk_id_cur': ['exact'],
            'nombre_mat': ['icontains'],
            'descripcion_mat': ['icontains'],
            'fecha_creacion_mat': ['exact'],
            'fecha_actualizacion_mat': ['exact'],
            'usuario_creacion_mat': ['icontains'],
            'usuario_actualizacion_mat': ['icontains'],
            'fk_id_car': ['exact'],
            'fk_id_malla': ['exact'],
            'codigo_mat': ['exact'],
            'fk_id_doc': ['exact'],
            'tipo_mat': ['icontains'],
        }

class NewsFilterModule(django_filters.FilterSet):
    class Meta:
        model = Module
        fields = {
            'id_mod': ['exact'],
            'nombre_mod': ['icontains'],
            'descripcion_mod': ['icontains'],
        }

class NewsFilterPeriod(django_filters.FilterSet):
    class Meta:
        model = Period
        fields = {
            'id_per': ['exact'],
            'fecha_inicio_per': ['exact'],
            'fecha_cierre_per': ['exact'],
            'rango_per': ['icontains'],
            'fecha_creacion_per': ['exact'],
            'fecha_actualizacion_per': ['exact'],
            'estado_per': ['icontains'],
            'usuario_creacion_per': ['icontains'],
            'usuario_actualizacion_per': ['icontains'],
        }

class NewsFilterPermissions(django_filters.FilterSet):
    class Meta:
        model = Permissions
        fields = {
            'id_prm': ['exact'],
            'fk_id_seg': ['exact'],
            'fk_id_prf': ['exact'],
            'permiso_visualizar_prm': ['exact'],
            'permiso_agregar': ['exact'],
            'permiso_editar': ['exact'],
            'permiso_eliminar': ['exact'],
            'permiso_imprimir': ['exact'],
        }

class NewsFilterprofile(django_filters.FilterSet):
    class Meta:
        model = profile
        fields = {
            'id_prf': ['exact'],
            'nombre_prf': ['icontains'],
            'descripcion_prf': ['icontains'],
        }

class NewsFilterprofileUsers(django_filters.FilterSet):
    class Meta:
        model = profileUsers
        fields = {
            'id_perusu': ['exact'],
            'fk_id_per': ['exact'],
            'fk_id_usu': ['exact'],
        }

class NewsFilterSecurity(django_filters.FilterSet):
    class Meta:
        model = Security
        fields = {
            'id_seg': ['exact'],
            'fk_id_mod': ['exact'],
            'nombre_seg': ['icontains'],
            'descripcion_seg': ['icontains'],
        }

class NewsFilterStudentRepresentatives(django_filters.FilterSet):
    class Meta:
        model = StudentRepresentatives
        fields = {
            'id_repest': ['exact'],
            'primer_apellido_repest': ['icontains'],
            'segundo_apellido_repest': ['icontains'],
            'nombre_repest': ['icontains'],
            'correo_repest': ['icontains'],
            'telefono_repest': ['icontains'],
            'fk_id_car': ['exact'],
            'foto_repest': ['icontains'],
        }

class NewsFilterStudents(django_filters.FilterSet):
    class Meta:
        model = Students
        fields = {
            'id_est': ['exact'],
            'cedula_est': ['icontains'],
            'primer_apellido_est': ['icontains'],
            'segundo_apellido_est': ['icontains'],
            'nombre_est': ['icontains'],
            'email_est': ['icontains'],
            'telefono_est': ['icontains'],
            'ciclo_est': ['icontains'],
            'fk_id_fac': ['exact'],
            'fk_id_car': ['exact'],
            'celular_est': ['icontains'],
            'genero_est': ['icontains'],
            'estado_civil_est': ['icontains'],
            'etnia_est': ['icontains'],
            'discapacidad_est': ['icontains'],
            'provincia_est': ['icontains'],
            'ciudad_est': ['icontains'],
            'parroquia_est': ['icontains'],
            'direccion_est': ['icontains'],
            'fk_id_per': ['exact'],
            'fk_id_usu': ['exact'],
        }

class NewsFilterTeacher(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'id_doc': ['exact'],
            'cedula_doc': ['icontains'],
            'primer_apellido_doc': ['icontains'],
            'segundo_apellido_doc': ['icontains'],
            'nombre_doc': ['icontains'],
            'abreviatura_titulo_doc': ['icontains'],
            'fotografia_doc': ['icontains'],
            'perfil_profesional_doc': ['icontains'],
            'telefono_doc': ['icontains'],
            'email_doc': ['icontains'],
            'oficina_doc': ['icontains'],
            'facebook_doc': ['icontains'],
            'twitter_doc': ['icontains'],
            'pagina_web_doc': ['icontains'],
            'fk_id_car': ['exact'],
            'fecha_creacion_doc': ['exact'],
            'fecha_actualizacion_doc': ['exact'],
            'usuario_creacion_doc': ['icontains'],
            'usuario_actualizacion_doc': ['icontains'],
            'fk_id_usu': ['exact'],
            'linkedin_doc': ['icontains'],
            'sexo_doc': ['icontains'],
        }

class NewsFilteruniversidad(django_filters.FilterSet):
    class Meta:
        model = universidad
        fields = {
            'id_uni': ['exact'],
            'nombre_uni': ['icontains'],
            'direccion_uni': ['icontains'],
            'ruc_uni': ['icontains'],
            'telefono_uni': ['icontains'],
            'mision_uni': ['icontains'],
            'vision_uni': ['icontains'],
            'email_uni': ['icontains'],
            'facebook_uni': ['icontains'],
            'twitter_uni': ['icontains'],
            'instagram_uni': ['icontains'],
            'pagina_web_uni': ['icontains'],
            'sede_uni': ['icontains'],
            'logo_uni': ['icontains'],
            'fecha_creacion_car': ['exact'],
            'fecha_actualizacion_car': ['exact'],
        }

class NewsFilterusers(django_filters.FilterSet):
    class Meta:
        model = users
        fields = {
            'id_usu': ['exact'],
            'correo_usu': ['icontains'],
            'password_usu': ['icontains'],
            'nombre_usu': ['icontains'],
            'apellido_usu': ['icontains'],
            'fk_id_prf': ['exact'],
            'estado_usu': ['exact'],
        }