import logging

from git import Repo
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic.base import View
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from apps.get_pages import get_pages
from apps.project.models import Project
from apps.project.forms import ProjectForm
from apps.users.models import UserProfile
from apps.project.serializers import ProjectSerializers
from TestPlatformWeb.settings import PROJECT_PATH

# Create your views here.
logger = logging.getLogger('stu')


class ProjectPagination(PageNumberPagination):
    """
    测试项目列表自定义分页
    """

    # 默认每页显示的个数
    page_size = 5
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100

class ProjectView(View):
    def get(self,request):
        return render(request,'project.html')

class ProjectListView(generics.ListAPIView):
    """
    测试项目列表页
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    # 分页
    pagination_class = ProjectPagination


# class ProjectView(View):
#     """
#     测试项目列表视图
#     """

# def get(self, request):
#     print(request.user)
#     project_form = ProjectForm()
#     # project = Project.objects.all()
#     search_keyword = request.GET.get('project_name')
#     search_type = request.GET.get('project_type')
#     print(search_type)
#     search_dict = {}
#     if search_keyword:
#         search_dict['name'] = search_keyword
#     if search_type:
#         search_dict['type'] = search_type
#     # if search_keyword:
#     #     project = Project.objects.filter(name__contains=search_keyword,type__contains=search_type)
#     project = Project.objects.filter(**search_dict)
#     # print(Project)
#
#     paginator_obj = Paginator(project, 10)  # 每页10条
#     request_page_num = request.GET.get('page', 1)
#     project_obj = paginator_obj.page(request_page_num)
#
#     total_page_number = paginator_obj.num_pages
#
#     project_list = get_pages(int(total_page_number), int(request_page_num))
#
#     return render(request, 'project.html', {'obj': project_obj, 'obj_list': project_list, 'obj_form': project_form})


class ProjectAddView(View):
    """
    项目新增页面
    """

    def get(self, request):

        user = UserProfile.objects.get(username=request.user)

        project_form = ProjectForm({'creator': user.username})

        return render(request, 'project_add.html', {'obj_form': project_form})

    def post(self, request):
        project_form = ProjectForm(request.POST)

        if project_form.is_valid():
            name = request.POST['name']
            type = request.POST['type']
            detail = request.POST['detail']
            creator = UserProfile.objects.get(username=request.user)
            project = Project(name=name, type=type, detail=detail, creator=creator)
            project.save()
        else:
            return render(request, 'project_add.html', {'error': project_form.errors})
        return HttpResponseRedirect(reverse('project_list'))


class ProjectEditView(View):
    """
    项目编辑页
    """

    def get(self, request, id):
        project = Project.objects.get(id=id)

        user = UserProfile.objects.get(username=project.creator)

        project_form = ProjectForm(
            {'name': project.name, 'type': project.type, 'creator': user.username, 'detail': project.detail})
        return render(request, 'project_edit.html', {'obj_form': project_form})

    def post(self, request, id):
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = Project.objects.get(id=id)
            project.name = request.POST['name']
            project.type = request.POST['type']
            project.detail = request.POST['detail']
            project.creator = UserProfile.objects.get(username=request.user)
            project.save()
        return HttpResponseRedirect(reverse('project_list'))


class ProjectSyncView(View):
    def post(self, request):
        logger.debug('ProjectSync request:{}'.format(request))
        print(request)
        print(request.body)
        print(dir(request))
        id = request.POST['project_id']
        logger.info('ProjectSync request id:{}'.format(id))
        project = Project.objects.get(id=id)
        logger.debug('ProjectSync Project {}'.format(project))
        repo = Repo(PROJECT_PATH)
        repo.clone(project.url)
