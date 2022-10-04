from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="MCU Review")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #ForeignKey is used to relate one User to all of the posts created by said User (One to many) and the on_delete is used to to the database to drop all posts created by User
    body = models.TextField()
    year = models.PositiveSmallIntegerField()
    #need to add min of 2000 and max of 2030 preferably as drop down menu
    rating = models.PositiveSmallIntegerField()
    #need to add min of 0 and max of 10
    director = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
