#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin

from apps.test_suite.models import Suites


class SuitesAdmin(object):
    list_display = ['suite_num', 'name', 'belong_project', 'creator', 'detail', 'add_time', 'edit_time']
    search_fields = ['suite_num', 'name', 'belong_project', 'creator']
    list_filter = ['suite_num', 'name', 'belong_project', 'creator']


xadmin.site.register(Suites, SuitesAdmin)
