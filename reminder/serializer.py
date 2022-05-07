from rest_framework import serializers
from reminder.models import Remainder
class android(serializers.ModelSerializer):
    class Meta:
        model=Remainder
        fields='__all__'
