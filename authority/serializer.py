from rest_framework import serializers
from authority.models import Authourity
class android(serializers.ModelSerializer):
    class Meta:
        model=Authourity
        fields='__all__'
