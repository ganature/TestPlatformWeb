#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include

from apps.project.views import ProjectListView,ProjectAddView,ProjectEditView, ProjectSyncView,ProjectView

app_name = 'project'
urlpatterns = [
    path('list/', ProjectView.as_view(), name='project_list'),
    path('list/list',ProjectListView.as_view(),name='project_list_json'),
    path('add/',ProjectAddView.as_view(),name='project_add'),
    path('edit/<int:id>/',ProjectEditView.as_view(), name='project_detail'),
    path('sync/', ProjectSyncView.as_view(),name='project_sync'),
]
