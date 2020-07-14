from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = HTMLField()
    profile_photo = CloudinaryField('image')
    bio = HTMLField()
    number = HTMLField()
    email = HTMLField()
    address = HTMLField()
    creat_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    @classmethod
    def get_profile_by_id(cls,id):
        profile = cls.objects.get(user__id = id)
        return profile

class Project(models.Model):
    title = HTMLField()
    landing_page_image = CloudinaryField('image')
    description = HTMLField()
    link = HTMLField()
    technologies = HTMLField()
    collaborators = HTMLField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @classmethod
    def get_profile_projects(cls,id):
        profile_projects = cls.objects.get(profile__id = id)
        return profile_projects

class Ratings(models.Model):
    
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    average = models.IntegerField(default=0)

    def __str__(self):
        return self.average