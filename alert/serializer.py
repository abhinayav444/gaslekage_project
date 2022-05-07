from rest_framework import serializers
from alert.models import Alert
class android(serializers.ModelSerializer):
    class Meta:
        model=Alert
        fields='__all__'
