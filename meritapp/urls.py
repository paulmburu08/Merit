from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^new/profile$', views.new_profile, name='new_profile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
]