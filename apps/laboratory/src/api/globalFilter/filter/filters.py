import django_filters
from apps.laboratory.src.models.area import Area
from apps.laboratory.src.models.areaLaboratory import AreaLaboratory
from apps.laboratory.src.models.hoursExecuted import HoursExecuted
from apps.laboratory.src.models.laboratory import Laboratory
from apps.laboratory.src.models.laboratoryCareer import LaboratoryCareer
from apps.laboratory.src.models.laboratorySoftware import LaboratorySoftware
from apps.laboratory.src.models.observationGuide import ObservationGuide
from apps.laboratory.src.models.practicalGuide import PracticalGuide
from apps.laboratory.src.models.reservation import Reservation
from apps.laboratory.src.models.reservationType import ReservationType
from apps.laboratory.src.models.software import Software
from apps.laboratory.src.models.softwareReservation import SoftwareReservation

class NewsFilterArea(django_filters.FilterSet):
    class Meta:
        model = Area
        fields = {
            'id_area': ['exact'],
            'nombre_area': ['icontains'],
            'descripcion_area': ['icontains'],
            'imagen_area': ['icontains'],
            'fecha_creacion_area': ['exact'],
            'fecha_actualizacion_area': ['exact'],
            'usuario_creacion_area': ['icontains'],
            'usuario_actualizacion_area': ['icontains'],
        }

class NewsFilterAreaLaboratory(django_filters.FilterSet):
    class Meta:
        model = AreaLaboratory
        fields = {
           'id_labarea': ['exact'],
           'fk_id_area': ['exact'],
           'fk_id_lab': ['exact'],
        }

class NewsFilterHoursExecuted(django_filters.FilterSet):
    class Meta:
        model = HoursExecuted
        fields = {
            'id_horeje': ['exact'],
            'fk_id_res': ['exact'],
            'inicio_horeje': ['exact'],
            'fecha_creacion_res': ['exact'],
            'fecha_actualizacion_res': ['exact'],
        }

class NewsFilterLaboratory(django_filters.FilterSet):
    class Meta:
        model = Laboratory
        fields = {
            'nombre_lab': ['icontains'],
            'descripcion_lab': ['icontains'],
            'fotografia1_lab': ['icontains'],
            'fotografia2_lab': ['icontains'],
            'fk_docente_responsable_lab': ['exact'],
            'fk_administrativo_responsable_lab': ['exact'],
            'fecha_creacion_lab': ['exact'],
            'fecha_actualizacion_lab': ['exact'],
            'usuario_creacion_lab': ['icontains'],
            'usuario_actualizacion_lab': ['icontains'],
            'tipo_lab': ['icontains'],
            'ubicacion_lab': ['icontains'],
            'color_lab': ['exact'],
            'fk_administrativo_responsable_secundario_lab': ['exact'],
            'siglas_lab': ['exact'],
            'paralelo_guia': ['exact'],
        }

class NewsFilterLaboratoryCareer(django_filters.FilterSet):
    class Meta:
        model = LaboratoryCareer
        fields = {
            'id_labcar': ['exact'],
            'fk_id_lab': ['exact'],
            'fk_id_car': ['exact'],
            'fecha_creacion_labcar': ['exact'],
            'fecha_actualizacion_labcar': ['exact'],
            'usuario_creacion_labcar': ['icontains'],
            'usuario_actualizacion_labcar': ['icontains'],
        }

class NewsFilterLaboratorySoftware(django_filters.FilterSet):
    class Meta:
        model = LaboratorySoftware
        fields = {
            'id_labsof': ['exact'],
            'fk_id_lab': ['exact'],
            'fk_id_sof': ['exact'],
        }

class NewsFilterObservationGuide(django_filters.FilterSet):
    class Meta:
        model = ObservationGuide
        fields = {
            'id_observacion': ['exact'],
            'fecha_observacion': ['exact'],
            'detalle_observacion': ['icontains'],
            'fk_id_guia': ['exact'],
            'fk_id_doc': ['exact'],
            'estado_observaciones_guia_practica': ['exact'],
        }

class NewsFilterPracticalGuide(django_filters.FilterSet):
    class Meta:
        model = PracticalGuide
        fields = {
            'id_guia': ['exact'],
            'numero_practica_guia': ['icontains'],
            'tema_guia': ['icontains'],
            'fecha_inicial_guia': ['exact'],
            'fecha_final_guia': ['exact'],
            'archivo_guia': ['icontains'],
            'fk_id_doc': ['exact'],
            'objetivo_guia': ['icontains'],
            'instrucciones_guia': ['icontains'],
            'resultados_esperados_guia': ['icontains'],
            'bibliografia_guia': ['icontains'],
            'fk_id_lab': ['exact'],
            'fecha_creacion_guia': ['exact'],
            'fecha_actualizacion_guia': ['exact'],
            'usuario_creacion_guia': ['icontains'],
            'usuario_actualizacion_guia': ['icontains'],
            'fk_id_per': ['exact'],
            'fk_id_cur': ['exact'],
            'fk_id_mat': ['exact'],
            'fk_id_malla': ['exact'],
            'area_guia': ['icontains'],
            'medidas_guia': ['icontains'],
            'instrumentos_guia': ['icontains'],
            'trabajopreparatorio_guia': ['icontains'],
            'actividades_guia': ['icontains'],
            'informacion_guia': ['icontains'],
            'fk_laboratorista_aprobado': ['exact'],
            'fk_director_aprobado': ['exact'],
            'fecha_laboratorista_aprobado': ['exact'],
            'fecha_director_aprobado': ['exact'],
            'hora_guia': ['exact'],
            'fk_id_lin': ['exact'],
            'fk_id_sub': ['exact'],
            'fk_id_coordinador_id_doc': ['icontains'],
            'fk_id_car': ['exact'],
            'paralelo_guia': ['exact'],
            'metodologia_guia': ['icontains'],
            'estado_guia_practica': ['exact'],
        }

class NewsFilterReservation(django_filters.FilterSet):
    class Meta:
        model = Reservation
        fields = {
            'id_res': ['exact'],
            'fk_id_tipres': ['exact'],
            'fk_id_doc': ['exact'],
            'fk_id_lab': ['exact'],
            'fk_id_area': ['exact'],
            'fk_id_guia': ['exact'],
            'tema_res': ['icontains'],
            'comentario_res': ['icontains'],
            'estado_res': ['exact'],
            'fecha_hora_res': ['exact'],
            'duracion_res': ['exact'],
            'numero_participantes_res': ['exact'],
            'descripcion_participantes_res': ['icontains'],
            'materiales_res': ['icontains'],
            'fecha_creacion_res': ['exact'],
            'fecha_actualizacion_res': ['exact'],
            'usuario_creacion_res': ['icontains'],
            'usuario_actualizacion_res': ['icontains'],
            'fecha_hora_fin_res': ['exact'],
            'observaciones_finales_res': ['icontains'],
            'asistencia_res': ['exact'],
            'guia_adjunta_res': ['icontains'],
            'curso_res': ['icontains'],
            'materia_res': ['icontains'],
            'fk_id_car': ['exact'],
            'paralelo_res': ['exact'],
            'tipo_texto_res': ['icontains'],
            'fk_id_usu': ['exact'],
            'software_res': ['icontains'],
            'tipo_res': ['exact'],
            'pedidodocente_res': ['exact'],
        }

class NewsFilterReservationType(django_filters.FilterSet):
    class Meta:
        model = ReservationType
        fields = {
            'id_tipres': ['exact'],
            'nombre_tipres': ['icontains'],
            'estado_tipres': ['exact'],
            'fecha_creacion_tipres': ['exact'],
            'fecha_actualizacion_tipres': ['exact'],
            'usuario_creacion_tipres': ['icontains'],
            'usuario_actualizacion_tipres': ['icontains'],
        }

class NewsFilterSoftware(django_filters.FilterSet):
    class Meta:
        model = Software
        fields = {
            'id_sof': ['exact'],
            'nombre_sof': ['icontains'],
            'tipolicencia_sof': ['icontains'],
            'cantidad_sof': ['exact'],
            'unidad_sof': ['exact'],
            'costounitario_sof': ['exact'],
            'costototal_sof': ['exact'],
            'aplicaciones_sof': ['icontains'],
            'caracteristicas_sof': ['icontains'],
            'fecha_creacion_sof': ['exact'],
            'fecha_actualizacion_sof': ['exact'],
            'usuario_creacion_sof': ['icontains'],
            'usuario_actualizacion_sof': ['icontains'],
            'imagen_sof': ['icontains'],
            'fecha_caducidad_sof': ['exact'],
            'enlace_sof': ['icontains'],
        }

class NewsFilterSoftwareReservation(django_filters.FilterSet):
    class Meta:
        model = SoftwareReservation
        fields = {
            'id_sofres': ['exact'],
            'fk_id_sof': ['exact'],
            'fk_id_res': ['exact'],
        }