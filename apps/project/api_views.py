#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from django.views.generic.base import View
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.decorators import action

from apps.project.models import Project
from apps.users.models import UserProfile
from apps.project.forms import ProjectForm
from apps.project.serializers import ProjectSerializers
from TestPlatformWeb.settings import BASE_DIR
from common.utils.views import CustomViewBase
from common.utils.response import JsonResponse


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


class ProjectViewSet(CustomViewBase):
    """
    测试项目列表页
    """
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializers
    # 分页
    pagination_class = ProjectPagination

    search_fields = ('name', 'type')

    @action(methods=['get'], detail=True, )
    def sync(self, request, pk):
        project = Project.objects.get(id=pk)
        project_path = BASE_DIR + '/project/' + project.name
        if project.status == 0:
            if os.path.exists(project_path):
                os.chdir(project_path)
                os.system("git pull")
                project.status = 1
                project.save()
            else:
                os.makedirs(project_path)
                print("git clone {} {}".format(project.url, project_path))
                os.system("git clone {} {}".format(project.url, project_path))
                project.status = 1
                project.save()
            return JsonResponse(data=[], code=200, msg='项目初始化成功')
        elif project.status == 1:
            os.chdir(project_path)
            os.system("git pull")
            project.status = 1
            project.save()
            return JsonResponse(code=200, msg='项目已更新')
        else:
            return JsonResponse(code=100, msg='更新失败')


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
            return Response(OrderedDict([("code", 200)]))
        except Exception as e:
            print(e)
            return Response(("code", 100), status=status.HTTP_400_BAD_REQUEST)
