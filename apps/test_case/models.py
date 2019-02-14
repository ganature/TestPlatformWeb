from django.db import models

from apps.users.models import UserProfile
from apps.test_suite.models import Suites


# Create your models here.

class TestCase(models.Model):
    """
        测试用例模型
        """
    case_type = (
        ('web', 'Web自动化'),
        ('app', 'App自动化'),
        ('inface', '接口自动化'),)
    case_status = (
        ('idle', '未执行'),
        ('success', '通过'),
        ('fail', '失败'),)
    case_level = (
        ('low', '低'),
        ('medium', '中'),
        ('high', '高'),)

    case_num = models.CharField(max_length=20, verbose_name=u'用例编号')
    name = models.CharField(max_length=18, verbose_name=u'用例标题')
    type = models.CharField(max_length=20, choices=case_type, default='web', verbose_name=u'用例类型')
    suite = models.ManyToManyField(Suites, verbose_name=u'测试集')
    expect = models.CharField(max_length=50, verbose_name=u'期望结果')
    status = models.CharField(max_length=20, choices=case_status, default='idle', verbose_name=u'结果')
    level = models.CharField(max_length=20, choices=case_level, default='low', verbose_name=u'用例级别')
    creator = models.ForeignKey(UserProfile, verbose_name=u'创建人', on_delete=models.SET_NULL, null=True, blank=True)
    detail = models.CharField(max_length=50, verbose_name=u'用例描述')
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'用例库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Steps(models.Model):
    """
    测试步骤模型
    """
    step_num = models.IntegerField(verbose_name=u'步骤顺序号')
    name = models.CharField(max_length=18, verbose_name=u'操作步骤名称')
    # keyword = models.ForeignKey(
    # UserKeywords, on_delete=models.SET_NULL, null=True, blank=True)
    creator = models.ForeignKey(UserProfile, verbose_name=u'创建人', on_delete=models.SET_NULL, null=True, blank=True)
    doc = models.CharField(max_length=50, verbose_name=u'操作步骤描述', null=True, blank=True)
    remark = models.TextField(max_length=200, verbose_name=u'备注', blank=True)
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name = u'操作步骤库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
