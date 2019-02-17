from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.

class EnvView(View):
    """
    测试环境列表页
    """

    def get(self, request):
        """ Todo env"""
