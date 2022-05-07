from django.db import models

# Create your models here.
class Precaution(models.Model):
    precaution_id = models.AutoField(primary_key=True)
    precautions = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'precaution'

