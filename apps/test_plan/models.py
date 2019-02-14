from django.db import models

from apps.project.models import Project


# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'计划名称')
    project = models.ForeignKey(Project, verbose_name=u'测试项目', on_delete=models.SET_NULL, null=True, blank=True)
    remark = models.TextField(max_length=200, verbose_name=u'备注', blank=True)
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'测试计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
