import json

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.core.paginator import Paginator

from apps.get_pages import get_pages
from apps.test_case.models import TestCase
from apps.users.models import UserProfile
from apps.project.models import Project
from apps.test_case.forms import CaseForm


# Create your views here.

class CaseView(View):
    """
    测试用例列表视图
    """

    def get(self, request):
        case_form = CaseForm()
        project_list = Project.objects.all()

        case = TestCase.objects.all()
        paginator_obj = Paginator(case, 10)  # 每页10条
        request_page_num = request.GET.get('page', 1)
        case_obj = paginator_obj.page(request_page_num)

        total_page_number = paginator_obj.num_pages

        case_list = get_pages(int(total_page_number), int(request_page_num))

        return render(request, 'case.html',
                      {'obj': case_obj, 'obj_list': case_list, 'project_list': project_list, 'obj_form': case_form})


class CaseAddView(View):
    """
    用例新增视图
    """

    def get(self, request):
        case_form = CaseForm()
        # print(case_form)
        # print(type(case_form))
        return render(request, 'case_add.html', {'obj_form': case_form})

    def post(self, request):
        case_form = CaseForm(request.POST)
        user = UserProfile.objects.get(username=request.user)
        if case_form.is_valid():
            case_num = request.POST['case_num']
            name = request.POST['name']
            type = request.POST['type']
            level = request.POST['level']
            creator = user
            case = TestCase(case_num=case_num, name=name, type=type, level=level, creator=creator)
            case.save()
            # return render(request,'robotTemplates/robot_case_list.html',{'error_code':100,'msg': '保存成功'})
            return HttpResponse(json.dumps({'error_code': 100, 'error_msg': "保存成功"}))
        return render(request, 'case.html')


class CaseEditView(View):
    """
    用例编辑视图
    """

    def get(self, request, id):
        case = TestCase.objects.get(id=id)
        case_form = CaseForm({'case_num': case.case_num, 'name': case.name, 'type': case.type, 'level': case.level})
        return render(request, 'case_edit.html', {'obj_form': case_form})

    def post(self, request):
        case_form = CaseForm(request.POST)
        user = UserProfile.objects.get(username=request.user)
        if case_form.is_valid():
            case_num = request.POST['case_num']
            name = request.POST['name']
            type = request.POST['type']
            level = request.POST['level']
            creator = user.username
            case = TestCase(case_num=case_num, name=name, type=type, level=level, creator=creator)
            case.save()
            return HttpResponse({'msg': '保存成功'})
        return render(request, 'case.html')
