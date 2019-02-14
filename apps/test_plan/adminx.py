#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from apps.test_plan.models import Plan


class PlanAdmin(object):
    list_display = ['name', 'project', 'remark', 'add_time', 'edit_time']
    search_fields = []
    list_filter = []


xadmin.site.register(Plan, PlanAdmin)
