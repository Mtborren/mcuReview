from logging import PlaceHolder
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Featured(models.Model):
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('home')



class Hero(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('home')



class Category(models.Model):
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name.title()
    
    def get_absolute_url(self):
        return reverse('home')



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # bio = models.TextField()

    def __str__(self):
        return str(self.user)



class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="MCU Review")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #ForeignKey is used to relate one User to all of the posts created by said User (One to many) and the on_delete is used to to the database to drop all posts created by User
    body = models.TextField()
    year = models.IntegerField()
    rating = models.IntegerField()
    director = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Uncategorized')
    featured = models.CharField(max_length=255)
    heroes = models.ManyToManyField(Featured, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')



# class Hero(models.Model):
#     name = models.CharField(max_length=255)


# class Movie(models.Model):
#     name = models.CharField(max_length=255)
#     heroes = models.ManyToManyField(Hero)
