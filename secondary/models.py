from django.db import models
from user.models import User
# Create your models here.
class SecondaryUser(models.Model):
    sc_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,to_field='user_id',on_delete=models.CASCADE)
    user_name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'secondary_user'


