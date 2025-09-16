from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Create your models here.

class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    image = CloudinaryField('neighborhood image',blank=True,null=True)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField(default=0,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     self.neighborhood_name

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def update_neighborhood_name(cls, id,name):
        return cls.objects.filter(id = id).update(neighborhood_name=name)

    @classmethod
    def update_neighborhood_occupants(cls, id,occ):
        return cls.objects.filter(id = id).update(occupants=occ)

    @classmethod
    def search_neighborhood(cls, search_term):
        return cls.objects.filter(neighborhood_name__icontains = search_term)



    def __str__(self) -> str:
       return self.neighborhood_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    family_name = models.CharField(max_length=50,null=True,blank=True)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    hood = models.ForeignKey(Neighborhood, on_delete=models.DO_NOTHING,null=True)
    family_email = models.EmailField(blank=True,null=True)
    family_members = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile_photo(cls, id,family_email):
        return cls.objects.filter(id = id).update(family_email=family_email)

    
    @classmethod
    def search_username(cls,search_term):
        return cls.objects.filter(user__username__icontains = search_term)


    def get_absolute_url(self):
        return reverse('profile',args=[str(self.id)])

        # return reverse('home')
    


    def __str__(self) -> str:
       return self.user.username

# Add the messages on the page of each 
class Meeting(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save_meeting(self):
        self.save()

    def delete_meeting(self):
        self.delete()

    @classmethod
    def update_meeting_title(cls, id,title):
        return cls.objects.filter(id = id).update(title=title)


    def __str__(self) -> str:
        return self.user.username

class Business(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('Business photo',blank=True,null=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    neighbor = models.ForeignKey(Neighborhood,on_delete=models.DO_NOTHING)
    business_email = models.EmailField()

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        return cls.objects.filter(name__icontains = search_term)

    @classmethod
    def update_business_name(cls, id,name):
        return cls.objects.filter(id = id).update(name=name)
 
    def __str__(self) -> str:
        return self.name





    

