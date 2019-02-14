# coding=utf-8
from django.db import models

from apps.project.models import Project
# Create your models here.

class Library(models.Model):
    name = models.CharField(
        max_length=50, verbose_name=u'Library名称', unique=True)
    doc = models.CharField(max_length=50, verbose_name=u'Library名描述')
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'公用测试库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Keyword(models.Model):
    """
    关键字模型
    """
    name = models.CharField(max_length=50, verbose_name=u'关键字名称')
    doc = models.CharField(max_length=50, verbose_name=u'关键字描述')
    library = models.ForeignKey(
        Library, verbose_name=u'所属Library', on_delete=models.SET_NULL, null=True, blank=True)
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'关键字库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Resource(models.Model):
    """
    关键字资源
    """
    name = models.CharField(max_length=50, verbose_name=u'Resource名称')
    doc = models.CharField(max_length=100, verbose_name=u'Resource描述')
    project = models.ForeignKey(
        Project, verbose_name=u'所属项目', on_delete=models.SET_NULL, null=True, blank=True)
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'Resource库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserKeywords(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'用户关键字名称')
    doc = models.CharField(max_length=100, verbose_name=u'用户关键字描述')
    resource = models.ForeignKey(
        Resource, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'所属Resource')
    keyword = models.ForeignKey(
        Keyword, on_delete=models.SET_NULL, null=True, blank=True)
    relate_user_keyword = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                            verbose_name=u'关联用户关键字')
    args=models.CharField(max_length=100,verbose_name=u'参数')
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'用户关键字库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name