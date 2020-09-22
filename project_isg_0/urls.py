from django.urls import path,include
from . import views

app_name='project_isg_0'

urlpatterns = [
    path('', views.home,name='home'),
]
