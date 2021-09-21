from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.neighborhood_name

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def update_neighborhood_name(cls, id,name):
        return cls.objects.filter(id = id).update(name=name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    hood = models.ForeignKey(Neighborhood, on_delete=models.DO_NOTHING,null=True)
    family_email = models.EmailField(blank=True,null=True)
    family_members = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile_photo(cls, id,profile_photo):
        return cls.objects.filter(id = id).update(profile_photo=profile_photo)


class Meeting(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.user.username

    def save_meeting(self):
        self.save()

    def delete_meeting(self):
        self.delete()


class Business(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    neighbor = models.ForeignKey(Neighborhood,on_delete=models.DO_NOTHING)
    business_email = models.EmailField()

    def __str__(self):
        self.name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def update_business_name(cls, id,name):
        return cls.objects.filter(id = id).update(name=name)


    

