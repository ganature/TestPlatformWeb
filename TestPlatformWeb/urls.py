"""TestPlatformWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include

import xadmin

from apps.users.views import IndexView, user_logout,LoginView

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),

    # rest_framework
    path('api_auth/',include('rest_framework.urls')),

    # 项目路由配置
    path('project/', include('project.urls', namespace='project')),

    # 测试用例路由配置
    path('case/', include('test_case.urls', namespace='case')),

    # 测试集路由配置
    path('suite/', include('test_suite.urls', namespace='suite')),

    # 测试计划路由配置
    path('plan/', include('test_plan.urls', namespace='plan')),

    # 测试环境路由配置
    path('env/',include('env_config.urls',namespace='env')),

]
