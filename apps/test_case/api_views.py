#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict

from apps.test_case.models import TestCase
from apps.test_case.serializers import CaseSerializers
from apps.users.serializers import UserSerializer


class CaseListView(generics.ListAPIView):
    """
    测试用例列表
    """
    serializer_class = CaseSerializers
    creator = UserSerializer()

    class Meta:
        model = TestCase
        fields = '__all__'


class CaseEditView(APIView):
    """
    测试用例编辑
    """