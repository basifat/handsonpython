from rest_framework import serializers
from yusers.models import Dancing


class DancingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dancing
        fields = '__all__'