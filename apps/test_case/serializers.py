from rest_framework import serializers

from apps.test_case.models import TestCase
from apps.users.serializers import UserSerializer


class CaseSerializers(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = TestCase
        fields = "__all__"
