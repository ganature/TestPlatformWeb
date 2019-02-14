#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
import os
import sys


class UserKeywordsInit(object):
    """
    用户自定义关键字
    """
    _module_suffix = 'Test.py'
    _cls_suffix = 'Test'
    _method_suffix = 'test'

    def __init__(self):
        self.data = []

    def get_module_obj(self, module_path):
        """
        :param module_path: 包名
        :return:
        """
        package = self.get_module_name(module_path)
        print('package :{}'.format(package))
        if os.path.dirname(module_path) not in sys.path:
            sys.path.append(os.path.dirname(module_path))
        return __import__(package, fromlist=True)

    def get_module_name(self, module_path):
        """
        返回模块名称
        :param module_path:
        :return:
        """
        if os.path.isfile(module_path):
            return inspect.getmodulename(module_path)
        else:
            raise FileExistsError('{} is not file'.format(module_path))

    def ischildof(self, obj, cls):
        """
        判断obj是否继承cls
        :param obj:
        :param cls: 目标类
        :return:
        """
        try:
            for i in obj.__bases__:
                if i is cls or isinstance(i, cls):
                    return True
            for i in obj.__bases__:
                if self.ischildof(i, cls):
                    return True
        except AttributeError:
            return self.ischildof(obj.__class__, cls)
        return False

    def get_clsname_from_module(self, module_path):
        """
        返回模块下以“Test”结尾的类的名称
        :param module_path:
        :return:
        """
        cls_name = []
        module_obj = self.get_module_obj(module_path)
        for m in dir(module_obj):
            if m.endswith(self._cls_suffix):
                cls_name.append(m)
        return cls_name

    def get_clsobj_from_module(self, cls_name, module_path):
        """
        返回
        :param cls_name:
        :return:
        """
        module_obj = self.get_module_obj(module_path)
        if hasattr(module_obj, cls_name):
            return getattr(module_obj, cls_name)()
        else:
            raise TypeError('{} is not expect type:object'.format(module_obj))

    def get_methodname_from_clsobj(self, cls_obj):
        """
        返回类的测试方法的列表
        :param cls_obj:
        :return:
        """
        method_names = []
        for m in dir(cls_obj):
            if m.startswith(self._method_suffix):
                method_names.append(m)
        return method_names

    def get_method_obj_from_clsobj(self, cls_obj, method_name):
        """
        返回测试方法对象
        :param cls_obj:
        :param method_name:
        :return:
        """
        return getattr(cls_obj, method_name)

    def get_args_from_methodobj(self, method_obj):
        """
        返回测试方法的参数和
        :param method_obj:
        :return:
        """
        return method_obj.__code__.co_varnames, method_obj.__code__.co_argcount - 1

    def get_all_test_from_module(self, module_path):
        cls_data = []
        module_data = {}
        module_data['module_name'] = self.get_module_name(module_path)
        module_data['module_path'] = module_path
        module_data['cls_detail'] = cls_data
        for c in self.get_clsname_from_module(module_path):
            cls_dict = {}
            method_data = []
            cls_dict["cls_name"] = c
            cls_obj = self.get_clsobj_from_module(c, module_path)
            for m in self.get_methodname_from_clsobj(cls_obj):
                method_dict = {}
                method_obj = self.get_method_obj_from_clsobj(cls_obj, m)
                method_dict["method_name"] = m
                method_dict["args_count"] = self.get_args_from_methodobj(method_obj)[1]
                method_dict["args_names"] = self.get_args_from_methodobj(method_obj)[0][1:]
                method_data.append(method_dict)
            cls_dict["method_detail"] = method_data
            cls_data.append(cls_dict)
        # print(cls_data)
        return module_data

    def get_all_test_modules_path(self, path):
        if len(os.listdir(path)):
            for d in os.listdir(path):
                tmp_path = os.path.join(path, d)
                if os.path.isfile(tmp_path) and tmp_path.endswith(self._module_suffix):
                    print(tmp_path)
                    self.data.append(self.get_all_test_from_module(tmp_path))
                elif os.path.isdir(tmp_path):
                    self.get_all_test_modules_path(tmp_path)

    def get_data(self):
        return self.data


if __name__ == '__main__':
    # c = UserKeywordsInit(module_path='E:\PycharmProjects\FlaskDemo\interface.py')
    # print(c.run())
    p = 'C:\\Users\\49885\PycharmProjects\TestPlatformWeb\\apps\keywords'
    # __import__(p)
    # print(inspect.getmembers(p))
    c = UserKeywordsInit()
    c.get_all_test_modules_path(p)
    print(c.get_data())
