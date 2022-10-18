from django import forms
from .models import Post, Category
from datetime import date

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

todays_date = date.today()
YEAR_CHOICES = [tuple([x,x]) for x in range(todays_date.year, 2000, -1)]
RATING_CHOICES = [tuple([x,x]) for x in range(1,11)] 

todays_date = date.today()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "header_image", "category", "year", "director", "body", "rating"]


        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=RATING_CHOICES, attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "header_image", "category", "year", "director", "body", "rating"]


        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),

        }