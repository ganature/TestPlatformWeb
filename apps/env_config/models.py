from django.db import models


# Create your models here.

class Env(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'环境名称')
    ip = models.GenericIPAddressField(verbose_name=u'环境ip')
    detail = models.CharField(max_length=30, verbose_name=u'环境详情')
    add_time = models.DateField(auto_now_add=True, verbose_name=u'创建时间')
    edit_time = models.DateField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        verbose_name=u'测试环境'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
