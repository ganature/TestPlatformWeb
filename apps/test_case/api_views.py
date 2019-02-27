#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


from apps.test_case.models import TestCase
from apps.test_case.serializers import CaseSerializers
from apps.users.serializers import UserSerializer
from common.utils.views import CustomViewBase
from common.utils.response import JsonResponse


class CasePagination(PageNumberPagination):
    """
    测试项目列表自定义分页
    """

    # 默认每页显示的个数
    page_size = 5
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class CaseListView(generics.ListAPIView):
    """
    测试用例列表
    """
    serializer_class = CaseSerializers
    creator = UserSerializer()

    class Meta:
        model = TestCase
        fields = '__all__'


class CaseViewSet(CustomViewBase):
    """
    测试用例
    """
    queryset = TestCase.objects.all().order_by('id')
    serializer_class = CaseSerializers
    # 分页
    pagination_class = CasePagination

    search_fields = ('name', )