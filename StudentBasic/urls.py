from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<class_id>[0-9]+)/$', views.classInfo, name='classInfo'),
    url(r'^create/', views.StudentCreate.as_view()),
    url(r'^sucess/', views.StudentCreateSuccess.as_view(), name='createSuccess')
]