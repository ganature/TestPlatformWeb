from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.validators import UniqueValidator

from apps.project.models import Project
from apps.users.models import UserProfile
from apps.users.serializers import UserSerializer


class CreatorPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(id=self.context['request'].user.id)
        return queryset


class ProjectSerializers(serializers.ModelSerializer):
    creator = CreatorPrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Project.objects.all())],
        min_length=8,
        error_messages={'invalid': "项目名称已存在", 'min_length': "名称长度不能小于8"}
    )

    class Meta:
        model = Project
        fields = "__all__"
