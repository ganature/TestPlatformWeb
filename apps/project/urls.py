#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from apps.project.views import ProjectView
from apps.project.api_views import ProjectListView, ProjectSyncView, ProjectEditView, ProjectAddView, ProjectDeleteView

app_name = 'project'
urlpatterns = [
    path('list/', ProjectView.as_view(), name='project_list'),

    # api路由配置
    path('api/list', ProjectListView.as_view(), name='api_project_list'),
    path('api/add/', ProjectAddView.as_view(), name='project_add'),
    path('api/edit/<int:pk>', ProjectEditView.as_view(), name='project_detail'),
    path('api/delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    path('api/sync/', ProjectSyncView.as_view(), name='project_sync'), ]
