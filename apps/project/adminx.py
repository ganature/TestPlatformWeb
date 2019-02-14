#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from apps.project.models import Project


class ProjectAdmin(object):
    list_display = ['name', 'type', 'url', 'add_time', 'edit_time']
    search_fields = ['name', 'type']
    list_filter = ['name', 'type']


xadmin.site.register(Project, ProjectAdmin)
