#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from apps.test_case.models import TestCase


class TestCaseAdmin(object):
    list_display = ['case_num', 'name', 'type', 'suite', 'expect', 'status', 'level', 'creator', 'detail', 'add_time',
                    'edit_time']
    search_fields = ['case_num', 'name', 'type', 'suite', 'creator']
    list_filter = []


xadmin.site.register(TestCase, TestCaseAdmin)
