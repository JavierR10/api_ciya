from django.db import models
from django.utils import timezone
from .base import BaseModel
from apps.public.src.models.collegeCareer import CollegeCareer
from apps.public.src.models.teacher import Teacher
from apps.investigacion.src.models.projectType import ProjectType

class Project(BaseModel):
    id_pro = models.AutoField(primary_key=True)
    nombre_pro = models.TextField()
    fk_id_car = models.ForeignKey(CollegeCareer, on_delete=models.RESTRICT, to_field='id_car')
    fk_id_doc = models.ForeignKey(Teacher, on_delete=models.RESTRICT, to_field='id_doc')
    grupo_investigacion_pro = models.IntegerField()
    programa_pro = models.IntegerField()
    fk_id_tip = models.ForeignKey(ProjectType, on_delete=models.RESTRICT, to_field='id_tip')
    fk_id_lin = models.IntegerField()
    fecha_aprobacion_pro = models.IntegerField()
    fk_id_lin = models.IntegerField()

    def delete(self):
        self.deleted_at = timezone.now()  # Establecer la fecha de eliminación
        self.save()

        
        # Actualizar objetos relacionados
        related_objects = self._meta.related_objects
        for related_object in related_objects:
            related_model = related_object.related_model
            related_name = related_object.get_accessor_name()
            related_field_name = related_object.field.name
            related_queryset = getattr(self, related_name).all()
            related_queryset.update(deleted_at=timezone.now())
    
    class Meta:
        db_table = 'investigacion\".\"proyecto'

