from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.

class PlanView(View):
    """
    测试计划列表页
    """

    def get(self, request):
        """ Todo plan list page"""
        return render(request, 'plan.html')
