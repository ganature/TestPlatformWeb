from rest_framework import serializers

from apps.users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ["username", ]
