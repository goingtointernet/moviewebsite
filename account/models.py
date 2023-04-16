from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_img = models.ImageField(upload_to = 'profile_img', null = True, blank = True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = User.objects.get(id=self.id)
            if this.profile_img != self.profile_img:
                this.profile_img.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(User, self).save(*args, **kwargs)