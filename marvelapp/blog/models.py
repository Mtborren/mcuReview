from logging import PlaceHolder
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


# RATING_CHOICES = (
#     ('one', '1'),
#     ('two', '2'),
#     ('three', '3'),
#     ('four', '4'),
#     ('five', '5'),
#     ('six', '6'),
#     ('seven', '7'),
#     ('eight', '8'),
#     ('nine', '9'),
#     ('ten', '10'),
# )

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="MCU Review")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #ForeignKey is used to relate one User to all of the posts created by said User (One to many) and the on_delete is used to to the database to drop all posts created by User
    body = models.TextField()
    year = models.IntegerField()
    #need to add min of 2000 and max of 2030 preferably as drop down menu
    rating = models.IntegerField()
    # rating = models.CharField(max_length=10, choices=RATING_CHOICES, default='')
    #need to add min of 0 and max of 10
    director = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Uncategorized')


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
