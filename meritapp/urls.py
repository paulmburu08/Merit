from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/profile$', views.new_profile, name='new_profile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/project$', views.new_project, name='new_project'),
]