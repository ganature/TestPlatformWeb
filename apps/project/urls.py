#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.project.views import ProjectView
from apps.project.api_views import ProjectViewSet


api_list = ProjectViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)

api_detail = ProjectViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

router = DefaultRouter()
router.register(r'api', ProjectViewSet)
app_name = 'project'



urlpatterns = [
    path('list/', ProjectView.as_view(), name='project_list'),

    # api路由配置
    path('', include(router.urls))
    ]

