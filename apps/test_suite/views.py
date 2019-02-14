from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic.base import View
from django.core.paginator import Paginator

from apps.get_pages import get_pages
from apps.test_suite.models import Suites
from apps.users.models import UserProfile
from apps.test_suite.forms import SuiteForm


# Create your views here.

class SuiteView(View):
    """
    测试集列表页
    """

    def get(self, request):
        suite = Suites.objects.all()
        paginator_obj = Paginator(suite, 10)
        request_page_num = request.GET.get('page', 1)
        suite_obj = paginator_obj.page(request_page_num)
        total_page_number = paginator_obj.num_pages
        suite_list = get_pages(int(total_page_number), int(request_page_num))

        return render(request, 'suite.html', {'obj': suite_obj, 'obj_list': suite_list})


class SuiteAddView(View):
    """
    测试集新增页
    """

    @staticmethod
    def get(request):
        suiteform = SuiteForm()
        return render(request, 'suite_add.html', {'obj_form': suiteform})

    @staticmethod
    def post(request):
        suiteform = SuiteForm(request.POST)
        if suiteform.is_valid():
            suiteform.save(commit=True)
            return render(request, 'suite.html', {'msg': '保存成功'})
        else:
            error = suiteform.errors
            return render(request, 'suite_add.html', {'suiteform': suiteform, 'error': error})


class SuiteEditView(View):
    """
    项目编辑页
    """

    def get(self, request, id):
        suite = Suites.objects.get(id=id)

        user = UserProfile.objects.get(username=suite.creator)

        suite_form = SuiteForm(
            {'name': suite.name, 'type': suite.type, 'creator': user.username, 'detail': suite.detail})
        return render(request, 'suite_edit.html', {'obj_form': suite_form})

    def post(self, request, id):
        suite_form = SuiteForm(request.POST)
        if suite_form.is_valid():
            suite = Suites.objects.get(id=id)
            suite.name = request.POST['name']
            suite.creator = UserProfile.objects.get(username=request.user)
            suite.save()
        return HttpResponseRedirect(reverse('project_list'))