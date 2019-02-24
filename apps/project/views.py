
# -*- coding: utf-8 -*-
import logging
import os

from git import Repo
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse,Http404
from django.views.generic.base import View


from apps.project.models import Project
from apps.project.forms import ProjectForm
from apps.users.models import UserProfile
from TestPlatformWeb.settings import BASE_DIR


# Create your views here.
# logger = logging.getLogger('debug')


class ProjectView(View):
    def get(self, request):
        project_from=ProjectForm()
        return render(request, 'project.html',{"obj_form":project_from})





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



