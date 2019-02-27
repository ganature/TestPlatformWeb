from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.test_suite.views import SuiteView, SuiteAddView, SuiteEditView
from apps.test_suite.api_views import SuitesViewSet

api_list = SuitesViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)

api_detail = SuitesViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

router = DefaultRouter()
app_name = 'suite'

router.register(r'api', SuitesViewSet)

urlpatterns = [
    path('list/', SuiteView.as_view(), name='suite_list'),
    # path('add/', SuiteAddView.as_view(), name='suite_add'),
    # path('edit/<int:id>/', SuiteEditView.as_view(), name='suite_edit'),

    path('', include(router.urls)),

]
