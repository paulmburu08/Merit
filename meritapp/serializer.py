from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'profile_photo', 'bio', 'number', 'email', 'address')

# class ProjectsSerializer(serializers.ModelSerializer):
#     projects = ProfileSerializer(many = True, read_only= True)
#     class Meta:
#         model = Project
#         fields = ('get_profile_projects')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','landing_page_image','description','link')