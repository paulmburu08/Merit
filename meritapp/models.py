from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = HTMLField()
    profile_photo = CloudinaryField('image')
    bio = HTMLField()
    creat_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name