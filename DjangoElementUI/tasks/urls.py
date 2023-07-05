from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [
    # 创建活动
    path('create/', views.task_create, name='task_create'),


    # Retrieve task list
    path('', views.task_list, name='task_list'),

    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),

    # 更新活动
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),

    # 删除活动
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
#主页显示注册用户以及任务数量
     path('tasks/dashboard/', views.dashboard, name='dashboard'),
]


   
