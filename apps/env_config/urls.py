from django.urls import path

from apps.env_config.views import EnvView
app_name = 'env'
urlpatterns = [path('list/', EnvView.as_view(), name='env_list')]