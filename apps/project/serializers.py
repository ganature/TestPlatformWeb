from rest_framework import serializers

from apps.project.models import Project
from apps.users.serializers import UserSerializer


class ProjectSerializers(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Project
        fields = "__all__"
