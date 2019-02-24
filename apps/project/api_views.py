#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict

from apps.project.models import Project
from apps.users.models import UserProfile
from apps.project.forms import ProjectForm
from apps.project.serializers import ProjectSerializers
from TestPlatformWeb.settings import BASE_DIR


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


class ProjectAddView(APIView):
    """
    项目新增页面
    """

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Exception as e:
            pass

    def post(self, request):
        print(request.POST)
        project = Project.objects.all()
        serializer = ProjectSerializers(project, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            data = {
                "error_code": 0,
                "error_msg": "ok",
                "data": serializer.data,
                }
            return Response(data=data)
        else:
            data = {
                "data": serializer.errors,
                }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class ProjectEditView(APIView):
    """
    项目编辑
    """

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Exception as e:
            pass

    def get(self, request):
        pk = request.GET['pk']
        project = self.get_object(pk)
        serializer = ProjectSerializers(project)
        data = {
            "error_code": 0,
            "error_msg": "ok",
            "data": serializer.data,
            }
        return Response(data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializers(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectSyncView(APIView):

    def post(self, request):
        id = request.POST['project_id']
        print('ProjectSync request id:{}'.format(id))
        project = Project.objects.get(id=id)
        project_path = BASE_DIR + '/project/' + project.name
        print("project_path : {}".format(project_path))
        print(project_path)
        try:
            if os.path.exists(project_path):
                os.chdir(project_path)
                os.system("git pull")
            else:
                os.makedirs(project_path)
                print("git clone {} {}".format(project.url, project_path))
                os.system("git clone {} {}".format(project.url, project_path))
                # os.system("git clone {}".format(project.url))
            return Response(OrderedDict([("status_code", 200)]))
        except Exception as e:
            print(e)
            return Response(("status_code", 100), status=status.HTTP_400_BAD_REQUEST)
