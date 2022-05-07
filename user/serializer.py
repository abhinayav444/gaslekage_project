from rest_framework import serializers
from user.models import User
from user.models import AddLocation

class android(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class android1(serializers.ModelSerializer):
    class Meta:
        model=AddLocation
        fields='__all__'
