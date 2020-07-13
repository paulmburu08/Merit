from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^new_profile$', views.new_profile, name='new_profile'),
     url(r'^profile/(\d+)', views.profile, name='profile'),
]