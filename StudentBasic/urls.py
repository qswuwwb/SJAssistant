from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^(?P<class_id>[0-9]+)/$', views.classInfo, name='classInfo')
]