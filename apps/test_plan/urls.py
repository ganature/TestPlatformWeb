from django.urls import path,include

from apps.test_plan.views import PlanView
app_name = 'plan'
urlpatterns = [
    path('list/', PlanView.as_view(), name='plan_list')
]
