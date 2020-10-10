from rest_framework import serializers
from yaasusers.models import YaasUser


class YaasUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = YaasUser
        fields = ('username', 'password', 'email')
        write_only_fields = ('password',)
        # read_only_fields = ('id',)

    def create(self, validated_data):
        user = YaasUser.objects.create(
            username=validated_data['username'], 
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user