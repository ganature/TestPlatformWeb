from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator

from apps.get_pages import get_pages


# Create your views here.

class PlanView(View):
    """
    测试计划列表页
    """

    def get(self, request):
        """ Todo plan list page"""
        return render(request, 'plan.html')
