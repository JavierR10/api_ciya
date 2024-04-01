from django.db import models

class AssociatedDocument(models.Model):
    id_aso = models.AutoField(primary_key=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_doc_asociado = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'academico\".\"documento_asociado'

