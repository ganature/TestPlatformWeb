from django.urls import path,include
from rest_framework.routers import DefaultRouter

from apps.test_plan.views import PlanView
from apps.test_plan.api_views import PlanViewSet

api_list = PlanViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)

api_detail = PlanViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

router = DefaultRouter()
app_name = 'plan'

router.register(r'api', PlanViewSet)
urlpatterns = [
    path('list/', PlanView.as_view(), name='plan_list'),

    path('', include(router.urls)),
]
