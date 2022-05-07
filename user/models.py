from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    post_office = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    district = models.CharField(max_length=25)
    gender = models.CharField(max_length=15)
    email_id = models.CharField(max_length=25)
    state = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user'

class AddLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=25)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'add_location'
