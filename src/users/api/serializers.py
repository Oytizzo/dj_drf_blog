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


# testing
class Prfl(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']


class UserProfileSerializer(serializers.ModelSerializer):
    profile = Prfl()

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'profile']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.save()

        return instance


# stackoverflow
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['image']
#
#
# class UpdateUserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()
#
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'profile']
#
#     def update(self, instance, validated_data):
#         # We try to get profile data
#         profile_data = validated_data.pop('profile', None)
#         # If we have one
#         if profile_data is not None:
#             # We set address, assuming that you always set address
#             # if you provide profile
#             instance.profile.address = profile_data['address']
#             # And save profile
#             instance.profile.save()
#         # Rest will be handled by DRF
#         return super().update(instance, validated_data)
