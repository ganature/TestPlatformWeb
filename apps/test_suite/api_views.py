#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


from apps.test_suite.models import Suites
from apps.test_suite.serializers import SuitesSerializers
from apps.users.serializers import UserSerializer
from common.utils.views import CustomViewBase
from common.utils.response import JsonResponse


class SuitesPagination(PageNumberPagination):
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


class SuitesViewSet(CustomViewBase):
    """
    测试用例列表
    """
    serializer_class = SuitesSerializers
    # 分页
    pagination_class = SuitesPagination



