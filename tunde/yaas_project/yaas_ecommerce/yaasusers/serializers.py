from rest_framework import serializers
from yaasusers.models import YaasUser, YaasUserLanguage


class YaasUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = YaasUser
        fields = ('username', 'password', 'email', 'language')
        write_only_fields = ('password',)
        # read_only_fields = ('id',)

    def create(self, validated_data):
        user = YaasUser.objects.create(
            username=validated_data['username'], 
            email=validated_data['email'],
            language=validated_data['language']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class YaasUserLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = YaasUserLanguage
        fields = '__all__'
            #write_only_fields = ('password',)
            # read_only_fields = ('id',)