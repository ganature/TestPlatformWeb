# Generated by Django 2.0.5 on 2019-02-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='环境名称')),
                ('ip', models.GenericIPAddressField(verbose_name='环境ip')),
                ('detail', models.CharField(max_length=30, verbose_name='环境详情')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('edit_time', models.DateField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '测试环境',
                'verbose_name_plural': '测试环境',
            },
        ),
    ]
