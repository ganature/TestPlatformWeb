#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from apps.project.views import ProjectView,ProjectAddView
from apps.project.api_views import ProjectListView, ProjectSyncView, ProjectEditView

app_name = 'project'
urlpatterns = [
    path('list/', ProjectView.as_view(), name='project_list'),

    path('add/', ProjectAddView.as_view(), name='project_add'),
    path('edit/', ProjectEditView.as_view(), name='project_detail'),
    path('sync/', ProjectSyncView.as_view(), name='project_sync'),
    # api路由配置
    path('api/list', ProjectListView.as_view(), name='project_list_json'),
    ]
