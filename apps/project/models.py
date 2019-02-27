from django.db import models

from apps.users.models import UserProfile


# Create your models here.

class Project(models.Model):
    """
        项目模型
    """
    project_type = (
        ('web', 'Web自动化'),
        ('app', 'App自动化'),
        ('inface', '接口自动化')
    )
    project_status = (
        (0, 'init'),
        (1, 'normal')
    )

    name = models.CharField(max_length=30, verbose_name=u'项目名称')
    type = models.CharField(max_length=30, choices=project_type, verbose_name=u'项目类型')
    url = models.CharField(max_length=100, verbose_name=u'项目地址')
    status = models.CharField(default=0, choices=project_status, max_length=30, verbose_name=u'状态')
    creator = models.ForeignKey(UserProfile, verbose_name=u'创建人', on_delete=models.SET_NULL, null=True, blank=True)
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'测试项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
