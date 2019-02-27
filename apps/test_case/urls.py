from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.test_case.views import CaseView, CaseAddView, CaseEditView
from apps.test_case.api_views import CaseViewSet

api_list = CaseViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)

api_detail = CaseViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

router = DefaultRouter()
app_name = 'case'

router.register(r'api', CaseViewSet)

urlpatterns = [
    path('list/', CaseView.as_view(), name='case_list'),

    # api视图路由
    path('', include(router.urls), name='api_case'),

]
