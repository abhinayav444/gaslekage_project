from rest_framework import serializers
from secondary.models import SecondaryUser
class android(serializers.ModelSerializer):
    class Meta:
        model=SecondaryUser
        fields='__all__'
