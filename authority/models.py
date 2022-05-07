from django.db import models

# Create your models here.
class Authourity(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=25)
    branch_loc = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    helpline_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'authourity'

