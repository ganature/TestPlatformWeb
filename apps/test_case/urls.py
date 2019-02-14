from django.urls import path, include

from apps.test_case.views import CaseView, CaseAddView, CaseEditView

app_name = 'case'
urlpatterns = [
    path('list/', CaseView.as_view(), name='case_list'),
    path('add/', CaseAddView.as_view(), name='case_add'),
    path('edit/<int:id>/', CaseEditView.as_view(), name='case_edit'),
]
