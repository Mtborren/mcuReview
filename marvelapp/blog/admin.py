from django.contrib import admin
from .models import Post, Category, Profile, Featured
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Featured)


