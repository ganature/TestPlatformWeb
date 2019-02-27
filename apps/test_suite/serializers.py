from rest_framework import serializers

from apps.test_suite.models import Suites


class SuitesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Suites
        fields = "__all__"
