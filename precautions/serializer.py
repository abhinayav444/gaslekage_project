from rest_framework import serializers
from precautions.models import Precaution
class android(serializers.ModelSerializer):
    class Meta:
        model=Precaution
        fields='__all__'
