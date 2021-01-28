from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='new_post/', blank = 'true')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', null=True)

    def save_profile(self):
        self.save

    def delete_user(self):
        self.delete()

   
    def __str__(self):
        return f'{self.user.username} Profile'