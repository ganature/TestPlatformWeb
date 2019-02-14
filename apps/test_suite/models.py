#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from apps.project.models import Project
from apps.users.models import UserProfile


# Create your models here.
class Suites(models.Model):
    """
    测试集模型
    """
    suite_num = models.CharField(max_length=20, verbose_name=u'测试集编号')
    name = models.CharField(max_length=18, verbose_name=u'测试集名称')
    belong_project = models.ForeignKey(Project, verbose_name=u'所属项目', on_delete=models.SET_NULL, null=True, blank=True)
    creator = models.ForeignKey(UserProfile, verbose_name=u'创建人', on_delete=models.SET_NULL, null=True, blank=True)
    detail = models.CharField(max_length=50, verbose_name=u'测试集描述')
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'测试集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
