from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    bio = models.TextField(max_length=500, blank=True, default='No bio')

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
         if created:
            Profile.objects.create(user=instance)
            instance.profile.save()   


class Subject(models.Model):
    name = models.CharField(max_length =30)
   
    def __str__(self):
        return self.name    

    def save_subject(self):
        self.save()
    
    @classmethod
    def get_subjects(cls):
        subjects = Subject.objects.all()
        return subjects


class Card(models.Model):
    title = models.CharField(max_length=50)
    note = HTMLField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cards')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ["-pk"]


    def save_card(self):
        self.save()    

    def delete_card(self):
        self.delete()

    def __str__(self):
        return self.title    

    @classmethod
    def filter_by_subject(cls, subject):
        card = Card.objects.filter(subject__name=subject).all()
        return card    

