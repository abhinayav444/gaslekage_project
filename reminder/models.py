from django.db import models

# Create your models here.
class Remainder(models.Model):
    remainder_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    alert_mode = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'remainder'

