from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.project.models import Project


class ProjectSerializers(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Project.objects.all(), message="项目名称已存在")],
        min_length=8,
        error_messages={'min_length': "名称长度不能小于8"}
    )

    class Meta:
        model = Project
        fields = "__all__"
