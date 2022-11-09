from django import forms
from .models import Post, Featured, Category
from datetime import date



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "header_image", "category", "featured", "heroes", "year", "director", "body", "rating"]


        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=Category.objects.all().values_list('name', 'name'), attrs={'class': 'form-control text-capitalize'}),
            'featured': forms.Select(choices=Featured.objects.all().values_list('name', 'name'), attrs={'class': 'form-control text-capitalize'}),
            'heroes': forms.CheckboxSelectMultiple(choices=Featured.objects.all().values_list('name', 'name'), attrs={'type':'checkbox', 'class': 'form-check text-capitalize'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.Select(choices=[tuple([x,x]) for x in range(date.today().year, 2000, -1)], attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=[tuple([x,x]) for x in range(10, 0, -1)] , attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "header_image", "category", "featured", "heroes", "year", "director", "body", "rating"]


        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=Category.objects.all().values_list('name', 'name'), attrs={'class': 'form-control text-capitalize'}),
            'featured': forms.Select(choices=Featured.objects.all().values_list('name', 'name'), attrs={'class': 'form-control text-capitalize'}),
            'heroes': forms.CheckboxSelectMultiple(choices=Featured.objects.all().values_list('name', 'name'), attrs={'type':'checkbox', 'class': 'text-capitalize'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.Select(choices=[tuple([x,x]) for x in range(date.today().year, 2000, -1)], attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=[tuple([x,x]) for x in range(10, 0, -1)] , attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),

        }