#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin

from apps.env_config.models import Env


class EnvAdmin(object):
    list_display = ['name', 'ip', 'detail', 'add_time', 'edit_time']
    search_fields = ['name', 'ip', 'detail', 'add_time', 'edit_time']
    list_filter = ['name', 'ip', 'detail', 'add_time', 'edit_time']


xadmin.site.register(Env, EnvAdmin)
