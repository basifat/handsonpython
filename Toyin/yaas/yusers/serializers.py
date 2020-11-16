from rest_framework import serializers
from yusers.models import Actors


class ActorsSerializer(serializers.ModelSerializer):
    #actor_id = serializers.IntegerField(required=False)

    # actor_id = serializers.IntegerField(label="Enter Actor Id")
    # name = serializers.CharField(label="Enter Actor Name")
    # email = serializers.EmailField(label="Enter Actor Email")
    # password = serializers.CharField(label="Enter Actor password")


    # def update(self, instance, validated_data):
    #     instance.actor_id = validated_data.get('actor_id', instance.actor_id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('body', instance.email)
    #     instance.password = validated_data.get('author_id', instance.password)

    #     instance.save()
    #     return instance

    class Meta:
        model = Actors
        fields = '__all__'


    # def create(self, validated_data):
    #     return Dancing.objects.create(**validated_data)

    
    