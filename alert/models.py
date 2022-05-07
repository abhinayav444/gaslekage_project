from django.db import models
from user.models import User
# Create your models here.
class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,to_field='user_id',on_delete=models.CASCADE)
    device_id = models.IntegerField()
    alert = models.CharField(max_length=11)
    alert_num = models.IntegerField()
    gas_level = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.CharField(max_length=11)
    longitude = models.CharField(max_length=11)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'alert'







