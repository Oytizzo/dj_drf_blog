from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import Profile

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "username", "email", "password",)


class PUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email']


# class ProfileSerializer(serializers.ModelSerializer):
#     user = ProfileUserSerializer()
#
#     class Meta:
#         model = Profile
#         fields = ['user', 'image']
#
#     def update(self, validated_data):
#         users_data = validated_data.pop('user')
#         profile = Profile.objects.create(**validated_data)
#         for user_data in users_data:
#             UserModel.objects.create(profile=profile, **user_data)
#         return profile


class ProfileSerializer(serializers.ModelSerializer):
    user = PUserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'image']

    def update(self, instance, validated_data):
        # users_data = validated_data.pop('user')
        instance.image = validated_data.get('image', instance.image)
        # for user_data in users_data:
        #     instance.user.username = user_data['username']
        #     instance.user.email = user_data['email']

        instance.save()
        return instance
