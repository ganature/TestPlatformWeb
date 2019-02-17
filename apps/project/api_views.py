#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from apps.project.models import Project
from apps.project.serializers import ProjectSerializers


class ProjectPagination(PageNumberPagination):
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


class ProjectListView(generics.ListAPIView):
    """
    测试项目列表页
    """
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializers
    # 分页
    pagination_class = ProjectPagination

