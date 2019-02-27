from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.test_case.models import TestCase


class CaseSerializers(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    case_num = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=TestCase.objects.all(),
                message="用例编号已存在"
            )
        ],
    )

    class Meta:
        model = TestCase
        fields = "__all__"
