from django.urls import path

from apps.test_suite.views import SuiteView, SuiteAddView, SuiteEditView
app_name = 'suite'
urlpatterns = [
    path('list/', SuiteView.as_view(), name='suite_list'),
    path('add/', SuiteAddView.as_view(), name='suite_add'),
    path('edit/<int:id>/', SuiteEditView.as_view(), name='suite_edit')

]
