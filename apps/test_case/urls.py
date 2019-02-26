from django.urls import path, include

from apps.test_case.views import CaseView, CaseAddView, CaseEditView
from apps.test_case.api_views import CaseListView as API_CaseListView

app_name = 'case'
urlpatterns = [
    path('list/', CaseView.as_view(), name='case_list'),
    path('add/', CaseAddView.as_view(), name='case_add'),
    path('edit/<int:id>/', CaseEditView.as_view(), name='case_edit'),

    # api视图路由
    path('api/list/',API_CaseListView.as_view(),name='api_case_list'),

]
