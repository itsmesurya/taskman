from django.conf.urls import url

from . import views

app_name='tasks'

urlpatterns = [
    url(r"^$", views.TaskList.as_view(), name="all"),
    url(r"new/$", views.CreateTask.as_view(), name="create"),
    url(r"by/(?P<username>[-\w]+)/$",views.UserTasks.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.TaskDetail.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeleteTask.as_view(),name="delete"),
    
]
